from sqlalchemy import create_engine
from sqlalchemy.sql import text
import pandas as pd 
import creds
import agate
import agatesql

connection_str = 'mysql://{}:{}@{}:{}/{}'.format(creds.uname,creds.pwd,creds.server,creds.port,creds.database)
engine = create_engine(connection_str)
connection = engine.connect()

#creating query for table creation 
file_path = r"C:\Users\Nirupam Bidikar\Downloads\extract_public_2018_20200216205325557_64460_20180102-20190101Texas\extract_public_2018_20200216205325_charges_20180102-20180302Texas.csv"
table_csv = agate.Table.from_csv(file_path) #create a var for table_name later
table_create_query = table_csv.to_sql_create_statement(table_name= "crashes", dialect= "mysql", db_schema= "main_database")

connection.execute(table_create_query)  #excute table  creation

import_query = text("LOAD DATA LOCAL INFILE :fp INTO TABLE `main_database`.`crashes` FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'")
results = connection.execute(import_query,fp=file_path) #execute file import to table
print(results)
