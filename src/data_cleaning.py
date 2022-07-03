import hashlib
import pandas as pd
import numpy as np
from pathlib import Path


def clean_violations(df: pd.DataFrame) -> pd.DataFrame:
    """
    This function cleans the 'Violations' columns of the main df. It splits the information out
    into 3 different columns ['number', 'comment', 'desc']. It also splits violations into
    their own distinct rows

    Args:
        df (pd.DataFrame): original dataframe

    Returns:
        pd.DataFrame: dataframe with 3 new columns
    """
    # convert violations to lowercase
    mask = df["Violations"].notna()
    df[mask, "Violations"] = df[mask, "Violations"].str.lower()
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
    # create comment and desc violation columns
    desc_split_reg = "- comments:"
    df.loc[exp_mask, "comment"] = (
        df.loc[exp_mask, "vio_temp"]
        .str.split(desc_split_reg)
        .apply(lambda x: x[-1] if len(x) > 1 else np.nan)
    )
    df.loc[exp_mask, "desc"] = (
        df.loc[exp_mask, "vio_temp"].str.split(desc_split_reg).apply(lambda x: x[0])
    )
    df = df.drop(columns=["vio_temp", "Violations"])
    return df


def clean_restaurants(df: pd.DataFrame) -> pd.DataFrame:
    return df


def clean_addresses(df: pd.DataFrame) -> pd.DataFrame:
    return df


def create_mappings(df: pd.DataFrame) -> pd.DataFrame:
    df["RestaurantId"] = df.apply(
        lambda x: abs(
            hash(str(x["DBA Name"]) + str(x["AKA Name"]) + str(x["Facility Type"]))
        )
        % (10**6),
        axis=1,
    )
    return df


if __name__ == "__main__":
    ##########################################
    # import data
    ##########################################
    data_path = Path(__file__).parents[1] / "data"
    dirty_data_path = data_path / "Food_Inspections.csv"
    og_df = pd.read_csv(dirty_data_path)

    ##########################################
    # Clean
    ##########################################
    # clean the violations
    inter_df = clean_violations(og_df)
    # clean restaurant table info
    inter_df = clean_restaurants(inter_df)
    # clean addresses df
    inter_df = clean_addresses(inter_df)
    # create columns for mapping between tables
    clean_df = create_mappings(inter_df)

    ##########################################
    # Save DFs
    ##########################################
    INS_COLS = []
    REST_COLS = []
    ADD_COLS = []
    # save off inspections df
    inspections_path = data_path / "inspection_table_df.csv"
    clean_df.to_csv(inspections_path)
    # save off restaurants df
    rest_path = data_path / "restaurant_table_df.csv"
    clean_df.to_csv(rest_path)
    # save off addresses df
    add_path = data_path / "addresses_table_df.csv"
    clean_df.to_csv(add_path)
