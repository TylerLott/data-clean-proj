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

#### For Dirty Data
1. Download the dataset `Food_Inspections.csv` from our team's [Box](https://uofi.app.box.com/folder/166723381455) account.

2. Place the downloaded dataset in the `./data/dirty_data` folder.

3. Run `python ./src/dirty/dirty_database.py`

#### For Clean Data
1. Download the dataset `Open_Refine_Inspections.csv` from our team's [Box](https://uofi.app.box.com/folder/166723381455) account.

2. Place the downloaded dataset in the `./data/clean_data` folder.

3. Run `python ./src/clean/data_cleaning.py`

4. Run `python ./src/clean/database.py`

## Final Submission

### Zip File

1. Workflow Model
   - [x] `data_cleaning.py`  
   - [x] `complete_wf_graph.gv`
   - [x] `complete_wf_graph_uri.gv`  
   <BR>

2. OpenRefine
   - [x] `OpenRefineHistory.json`  
   <BR>

3. Other Datacleaning Tools
   - [x] `data_cleaning.py`
   - [x] `notebooks/db_cleaning_exploration.ipynb`
   - [x] `notebooks/db_queries.ipynb`  
   <BR>

4. Queries
   - [x] `queries.txt`  
   <BR>

5. External links
   - [x] `DataLinks.txt`
      - [x] dirty data [Food_Inspections.csv](https://uofi.app.box.com/folder/166723381455)
      - [x] clean data
         - `EstablishmentInspections.csv`
         - `Establishment.csv`
         - `Inspections.csv`
      - [x] [GitHub](https://github.com/TylerLott/data-clean-proj)  
      <BR>

6. README
   - [x] create a `README.md` that explains the contents files in the zip folder  
   <BR>

### Box Folder

The follwoing files need to be in the box folder:

   - [x] `Food_Inspections.csv`

   - [x] `EstablishmentInspections.csv`

   - [x] `Establishment.csv`

   - [x] `Inspections.csv`

   
