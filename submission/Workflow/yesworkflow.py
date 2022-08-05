
##########################################
# OpenRefine
##########################################
# @BEGIN openrefine_cleaning
# @in Food_Inspections.csv
# @out Open_Refine_Inspections.csv

# @begin Type_Cleaning @description several columns have mixed data types, neet to convert to a consistent type.
# @in 
# @out
# @end Type_Cleaning

# @begin Establishment_Name_Clustering 
# @in Food_Inspections.csv
# @out 
# @end Establishment_Name_Clustering

# @end openrefine_cleaning


##########################################
# Data Cleaning
##########################################
# @BEGIN restaurant_inspection_pipeline @description Cleaning and Saves of Chicago Restaurant Inspections
# @in
# @out
# @BEGIN restaurant_inspection_import @description To read in the data from RestaurantInspections.csv
# @in restaurant_data_path @as Static_Restaruant @description CSV which contains restaurant inspection reviews
# @out restaurant_data_file @as RestaurantInspectionRead
# @end restaurant_inspection_import

# @BEGIN CleanRestaurantInspections @description Clean columns of the restaurant inspection data
# @in
# @out
# @BEGIN CleanViolations
# @in
# @out
# clean the violations
# inter_df = clean_violations(og_df)
# @end CleanViolations

# @BEGIN CleanEstablishments
# @in
# @out
# clean establishment table info
# inter_df = clean_establishments(inter_df)
# @end CleanRestaurants

##########################################
# IC Checks
##########################################
