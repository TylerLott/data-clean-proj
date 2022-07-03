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
    # create comment and desc violation columns
    desc_split_reg = "- comments:"
    df.loc[exp_mask, "comments"] = (
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
    """
    This function creates an id for a restaurant by taking the hash of the columns
    [DBA Name, AKA Name, Facility Type, Address, Latitude, Longitude]. This ensures rows with the same restaruant will
    have the same Id, so we are able to map between Inspection entry and Restaurant in the
    SQL tables

    Args:
        df (pd.DataFrame): original dataframe

    Returns:
        pd.DataFrame: dataframe with Id column
    """
    df["id"] = df.apply(
        lambda x: abs(
            hash(
                str(x["DBA Name"])
                + str(x["AKA Name"])
                + str(x["Facility Type"])
                + str(x["Address"])
                + str(x["Latitude"])
                + str(x["Longitude"])
            )
        ),
        axis=1,
    )
    return df


def rename_cols(df: pd.DataFrame) -> pd.DataFrame:
    cols = {
        "Inspection ID": "inspectionId",
        "DBA Name": "dbaName",
        "AKA Name": "akaName",
        "License #": "licenseNum",
        "Facility Type": "facilityType",
        "Risk": "risk",
        "Address": "address",
        "City": "city",
        "State": "state",
        "Zip": "zip",
        "Inspection Date": "date",
        "Inspection Type": "type",
        "Results": "results",
        "Latitude": "latitude",
        "Longitude": "longitude",
        "Location": "location",
    }
    return df.rename(columns=cols)


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
    inter_df = create_mappings(inter_df)
    clean_df = rename_cols(inter_df)

    ##########################################
    # Save DFs
    ##########################################
    INS_COLS = [
        "inspectionId",
        "licenseNum",
        "date",
        "type",
        "risk",
        "results",
        "number",
        "comments",
        "desc",
    ]
    REST_COLS = ["dbaName", "akaName", "facilityType", "id"]
    REST_INS_COLS = ["id", "inspectionId"]
    ADD_COLS = ["address", "city", "state", "zip", "location", "latitude", "longitude"]
    # save off inspections df
    inspections_path = data_path / "Inspections.csv"
    clean_df[INS_COLS].drop_duplicates().to_csv(inspections_path, index=False)
    # save off restaurants df
    rest_path = data_path / "Restaurants.csv"
    clean_df[REST_COLS].drop_duplicates().to_csv(rest_path, index=False)
    # save off relations df
    rest_ins_path = data_path / "RestaurantInspections.csv"
    clean_df[REST_INS_COLS].drop_duplicates().to_csv(rest_ins_path, index=False)
    # save off addresses df
    add_path = data_path / "Addresses.csv"
    clean_df[ADD_COLS].drop_duplicates().to_csv(add_path, index=False)
