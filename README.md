# Data Cleaning Project Part 2

## Getting Started

### For Windows

1. Get the dataset from [THIS KAGGLE LINK](https://www.kaggle.com/datasets/chicago/chi-restaurant-inspections), place the file in the data folder.

2. Ensure you have python 3.10 (you can probably use a lower version too)

3. run the following commands to set up the venv

   `python -m venv python_env`

   `./python_env/Scripts/activate`

   `python -m pip install -r requirements.txt`

4. Run `python ./src/data_cleaning.py`

5. Run `python ./src/database.py`

### For Mac

1. Get the dataset from [THIS KAGGLE LINK](https://www.kaggle.com/datasets/chicago/chi-restaurant-inspections), place the file in the data folder.

2. Ensure you have python 3.10 (you can probably use a lower version too)

3. run the following commands to set up the venv

   `python3.10 -m venv python_env`

   `source ./python_env/bin/activate`

   `python3.10 -m pip install -r requirements-mac.txt`

4. Run `python3.10 ./src/data_cleaning.py`

5. Run `python3.10 ./src/database.py`

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
