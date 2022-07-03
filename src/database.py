import pandas as pd
import sqlite3
from pathlib import Path


if __name__ == "__main__":
    data_path = Path(__file__).parents[1] / "data"
    # Create database
    db_path = data_path / "food_inspections.db"
    db = sqlite3.connect(db_path)

    tables = ["inspections", "restaurants", "addresses", "restaurantInspections"]

    # load in cleaned data
    for t in tables:
        p = data_path / str(t + ".csv")
        df = pd.read_csv(p)
        sql_load = df.to_sql(name=t, con=db)
