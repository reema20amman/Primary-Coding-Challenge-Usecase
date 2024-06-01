def udf_data_value(data, table_name):
    cnx = sqlite3.connect('C:/Users/USER/Downloads/Chinook_Sqlite.sqlite.db')
    data.to_sql(table_name, cnx)
    
df = pd.read_csv("C:/Users/USER/Downloads/machine-readable-business-employment-data-dec-2023-quarter.csv")
data_value = df[['Series_reference','Data_value', 'Period','STATUS','Group', 'Series_title_3']].groupby('STATUS').count().sort_values(by = ['Series_title_3'], ascending = True)
data_value

udf_data_value(data_value, 'table')
