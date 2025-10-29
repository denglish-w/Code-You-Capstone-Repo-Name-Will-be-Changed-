# CODE CURRENTLY DOESN'T WORK

try:
    import sqlite3
    import pandas as pd

# create the database

    connection = sqlite3.connect("database.db")

# import files
    housing_value = pd.read_csv('data/raw/hpi_po_metro.csv')

    unemployment = pd.read_csv('data/raw/ssamatab1.csv', skiprows=2)
    
# clean unemployment
    unemployment = unemployment.dropna(axis=1)

# create the tables in the database

    unemployment.to_sql("unemployment", connection, if_exists="replace", index=False)
    housing_value.to_sql("housing_value", connection, if_exists="replace", index=False)
except:
    print("Error creating database")