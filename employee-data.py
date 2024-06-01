import pandas as pd
import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError


df = pd.read_csv("C:/Users/USER/Downloads/business-employment-data.csv")
data_value = df[['Series_reference','Data_value', 'Period','STATUS','Group', 'Series_title_3']].groupby('STATUS').count().sort_values(by = ['Series_title_3'], ascending = True)
data_value     # execute the dataframe
udf_data_value(data_value, 'business_employee_table')

# Read CSV file into a dataframe
try:
    df = pd.read_csv('C:/Users/USER/Downloads/business-employment-data.csv')
except FileNotFoundError as e:
    print(f"Error reading CSV file: {e}")
    # Handle the error, maybe exit or log the error
    exit()

# Perform some operations 
try:
    # Your complex dataframe operations here
    df['new_column'] = df['old_column'] * 2
except KeyError as e:
    print(f"Error performing complex operations on dataframe: {e}")
    # Handle the error, maybe exit or log the error
    exit()

# Write the dataframe to a SQL database
try:
    engine = create_engine('C:/Users/USER/Downloads/Chinook_Sqlite.sqlite.db', echo=True)  # SQLite database example
    df.to_sql('table_name', con=engine, if_exists='replace', index=False)
    print("Dataframe written to SQL database successfully.")
except SQLAlchemyError as e:
    print(f"Error writing dataframe to SQL database: {e}")
    
