import os
import agate
import agatesql




file_path = r"C:\Users\Nirupam Bidikar\Downloads\extract_public_2018_20200216205325557_64460_20180102-20190101Texas\extract_public_2018_20200216205325_charges_20180102-20180302Texas.csv"
tab = agate.Table.from_csv(file_path)
que = tab.to_sql_create_statement(table_name= "crashes", dialect= "mysql", db_schema= "main_database")
print(que)
print(type(que))

