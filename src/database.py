import pandas as pd
import sqlite3


if __name__ == '__main__':
  # Create database
  db = sqlite3.connect('../data/food_inspections.db')

  # load in cleaned data
  df = pd.read_csv('../data/food_inspections_clean.csv')