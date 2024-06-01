import pandas as pd
import sqlite3

# connection for sql
cnx = sqlite3.connect('C:/Users/USER/Downloads/Chinook_Sqlite.sqlite')

df_customer = pd.read_sql_query('''
SELECT * FROM customer ''', cnx)
df_customer                                                  #display customer table
df_genre = pd.read_sql_query('''
SELECT * FROM genre ''', cnx)
df_genre                                                     #display genre table
df_track = pd.read_sql_query('''
SELECT * FROM track ''', cnx)
df_track                                                     #display track table
df_invoiceline = pd.read_sql_query('''
SELECT * FROM invoiceline ''', cnx)
df_invoiceline                                               #display invoiceline table
df_invoice = pd.read_sql_query('''
SELECT * FROM invoice ''', cnx)
df_invoice                                                   #display invoice table

# defining function to connect sql
def udf_write(data, table_name):
    cnx = sqlite3.connect('C:/Users/USER/Downloads/Chinook_Sqlite.sqlite.db')
    data.to_sql(cnx, table_name)

# merging multiple dataframe 
merged_df = pd.merge(
    
       pd.merge(
    
      pd.merge(
    
     pd.merge(
    
            df_genre, df_track, on = 'GenreId', how = 'inner'),
    
               df_invoiceline, on = 'TrackId', how = 'inner'),
    
                 df_invoice, on = 'InvoiceId', how = 'inner'),
    
                     df_customer, on = 'CustomerId', how = 'inner')

merged_df['Date'] = pd.to_datetime(merged_df['InvoiceDate'])

output = merged_df[['Name_x', 'FirstName', 'LastName', 'Total', 'Date']].query('Name_x.str.contains("Rock")').groupby(['Name_x', 'FirstName', 'LastName', 'Date'])['Name_x'].count()
#excuting data frame
df = pd.DataFrame(output)
df.rename(columns={'Name_x': 'count_values'}, inplace=True)
df    #display dataframe
# executing udf_write function to write to sql
table_data = udf_write(df, 'music_table')
