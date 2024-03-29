import pandas as pd
import numpy as np
import sqlite3
from pathlib import Path


def clean_violations(df: pd.DataFrame) -> pd.DataFrame:
    """
    This function cleans the 'Violations' columns of the main df. It splits the information out
    into 3 different columns ['number', 'comment', 'description']. It also splits violations into
    their own distinct rows

    Args:
        df (pd.DataFrame): original dataframe

    Returns:
        pd.DataFrame: dataframe with 3 new columns
    """
    # convert violations to lowercase
    mask = df["Violations"].notna()
    df.loc[mask, "Violations"] = df.loc[mask, "Violations"].str.lower()
    # create violation number column
    num_reg = r"(?:^|\| )(\d+\. )"
    vio_nums = df.loc[mask, "Violations"].str.extractall(num_reg)
    df.loc[mask, "number"] = vio_nums.groupby(level=0)[0].apply(list)
    # create violation_temp
    split_reg = r"(?:^|\| )\d+\. "
    df.loc[mask, "vio_temp"] = (
        df.loc[mask, "Violations"]
        .str.split(split_reg, regex=True)
        .apply(lambda x: x[1:])
    )
    # split into individual rows for violations
    df = df.explode(["vio_temp", "number"]).reset_index(drop=True)
    exp_mask = df["Violations"].notna()
    # create comment and description violation columns
    desc_split_reg = "- comments:"
    df.loc[exp_mask, "comments"] = (
        df.loc[exp_mask, "vio_temp"]
        .str.split(desc_split_reg)
        .apply(lambda x: x[-1] if len(x) > 1 else np.nan)
    )
    df.loc[exp_mask, "description"] = (
        df.loc[exp_mask, "vio_temp"].str.split(desc_split_reg).apply(lambda x: x[0])
    )
    df = df.drop(columns=["vio_temp", "Violations"])
    return df


def clean_establishments(df: pd.DataFrame) -> pd.DataFrame:
    return df


def create_mappings(df: pd.DataFrame) -> pd.DataFrame:
    """
    This function creates an id for a restaurant by taking the hash of the columns
    [DBA Name, Latitude, Longitude]. This ensures rows with the same restaruant will
    have the same Id, so we are able to map between Inspection entry and Restaurant in the
    SQL tables

    Args:
        df (pd.DataFrame): original dataframe

    Returns:
        pd.DataFrame: dataframe with Id column
    """
    df["estID"] = df.apply(
        lambda x: abs(
            hash( str(x["DBA Name"])
                + str(x["Latitude"])
                + str(x["Longitude"])
            )
        ),
        axis=1,
    )
    return df


def rename_cols(df: pd.DataFrame) -> pd.DataFrame:
    cols = {
            "DBA Name"          : "estName",
            "Inspection ID"     : "inspecID",
            "Results"           : "result",
            "Violations"        : "violations"
           }

    return df.rename(columns=cols)


if __name__ == "__main__":
    ##########################################
    # import data
    ##########################################
    # @BEGIN restaurant_inspection_pipeline @description Cleaning and Saves of Chicago Restaurant Inspections
    # @in
    # @out
    # @BEGIN restaurant_inspection_import @description To read in the data from RestaurantInspections.csv
    # @in restaurant_data_path @as Static_Restaruant @description CSV which contains restaurant inspection reviews
    # @out restaurant_data_file @as RestaurantInspectionRead
    data_path = Path(__file__).parents[2] / "data/dirty_data"
    dirty_data_path = data_path / "Food_Inspections.csv"
    og_df = pd.read_csv(dirty_data_path)
    # @end restaurant_inspection_import

    ##########################################
    # Clean
    ##########################################
    # @BEGIN CleanRestaurantInspections @description Clean columns of the restaurant inspection data
    # @in
    # @out
    # @BEGIN CleanViolations
    # @in
    # @out
    # clean the violations
    #inter_df = clean_violations(og_df)
    # @end CleanViolations

    # @BEGIN CleanEstablishments
    # @in
    # @out
    # clean establishment table info
    #inter_df = clean_establishments(inter_df)
    # @end CleanRestaurants

    # create columns for mapping between tables
    inter_df = create_mappings(og_df)
    dirty_df = rename_cols(inter_df)

    ##########################################
    # Save DFs
    ##########################################
    # inspection table's columns
    INS_COLS = ["inspecID", "result", "violations"]
    # save off inspections df
    inspections_path = data_path / "Inspections.csv"
    dirty_df[INS_COLS].drop_duplicates().to_csv(inspections_path, index=False)

    # establishment table's columns
    EST_COLS = ["estID", "estName"]
    # save off restaurants df
    est_path = data_path / "Establishments.csv"
    dirty_df[EST_COLS].drop_duplicates().to_csv(est_path, index=False)
    
    # establishment's inspections table's coulmns
    EST_INS_COLS = ["estID", "inspecID"]
    # save off relations df
    est_ins_path = data_path / "EstablishmentInspections.csv"
    dirty_df[EST_INS_COLS].drop_duplicates().to_csv(est_ins_path, index=False)

    ##########################################
    # Create database
    ##########################################
    db_path = data_path / "dirty_food_inspections.db"
    with sqlite3.connect(db_path) as con:

        tables = ["Establishments", "Inspections", "EstablishmentInspections"]

        # load in cleaned data
        for t in tables:
            p = data_path / str(t + ".csv")
            df = pd.read_csv(p)
            sql_load = df.to_sql(name=t, con=con, index=False)
