from sqlalchemy import create_engine
from sqlalchemy.sql import text
import pandas as pd 
from Database import creds
import agate
import agatesql
import ast


def connect():
    connection_str = 'mysql://{}:{}@{}:{}/{}?charset=utf8'.format(creds.uname,creds.pwd,creds.server,creds.port,creds.database)
    engine = create_engine(connection_str)
    connection = engine.connect()
    return connection

#creating query for table creation 
def upload_file(file_path, connection, table_name):
    table_csv = agate.Table.from_csv(file_path) #create a var for table_name later
    table_create_query = table_csv.to_sql_create_statement(table_name= table_name, dialect= "mysql", db_schema= "main_database")
    print(table_create_query)
    connection.execute(table_create_query)  #excute table  creation
    import_query = text("LOAD DATA LOCAL INFILE :fp INTO TABLE  `main_database`." + "`" +table_name + "`" + "FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'")
    connection.execute(import_query,fp=file_path,tn=table_name) #execute file import to table
    
def query(db_name,table_name, connection, offset_val=0):
    table_fetch_query = text("SELECT * FROM " + db_name + '.' + table_name + " LIMIT 30 OFFSET :of")
    columns_fetch_query = text("""SELECT `COLUMN_NAME` 
                                FROM `INFORMATION_SCHEMA`.`COLUMNS` 
                                WHERE `TABLE_SCHEMA`=:dn 
                                AND `TABLE_NAME`=:tn""")
    col_names = connection.execute(columns_fetch_query, dn= db_name, tn=table_name).fetchall()
    col_names_refined = [item for t in col_names for item in t]
    result = connection.execute(table_fetch_query,of=offset_val)
    reduced_result = result.fetchall()

    return col_names_refined,  reduced_result

def table_names(db_name,connection):
    tableNames_fetch_query = text("""SELECT `TABLE_NAME` 
                                FROM `INFORMATION_SCHEMA`.`TABLES` 
                                WHERE `TABLE_SCHEMA`=:dn""")
    table_names = connection.execute(tableNames_fetch_query, dn=db_name).fetchall()
    tableNames_refined = [item for t in table_names for item in t]
    return tableNames_refined
