# Data Cleaning Project Part 2

## Getting Started

### Setting Up Python Environment

Ensure you have python 3.10 (you can probably use a lower version too)

#### For Windows

1. Run the following commands to set up the venv:

   `python -m venv python_env`

   `./python_env/Scripts/activate`

   `python -m pip install -r requirements.txt`

#### For Mac

1. Run the following commands to set up the venv:

   `python3.10 -m venv python_env`

   `source ./python_env/bin/activate`

   `./python_env/bin/python3.10 -m pip install --upgrade pip`

   `python -m pip install -r requirements-mac.txt`

### Setting Up Project

1. Download the dataset `Inspections.csv` from our team's [Box](https://uofi.app.box.com/folder/166723381455) account.

2. Place the downloaded dataset in the data folder.

2. Run `python ./src/data_cleaning.py`

3. Run `python ./src/database.py`

## Creating the final Zip

1. collect everything from `workflow`, `notebooks`, `openRefine`, `src`, `queries`

   - rename anything that is unclear

2. collect the dirty data

   - this is the `Food_Inspections.csv` in the `data` dir

3. collect the clean data

   - these are `addresses.csv`, `inspections.csv`, `RestaurantInspections.csv`, and `restaurants.csv` from `data` dir

4. collect the `requirements.txt`

5. create a `README.md` file that breifly explains all of the files collected

6. put all these in a folder and zip it up
