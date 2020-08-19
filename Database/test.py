#this file is just for testing out functions 

import dbOps
from sqlalchemy import create_engine
from sqlalchemy.sql import text


#fp = r"C:\Users\Nirupam Bidikar\Downloads\TxDOT_Guardrail_End_Treatments.csv"
conn = dbOps.connect()
#fp = r"C:\Users\Nirupam Bidikar\Downloads\extract_public_2018_20200216205325557_64460_20180102-20190101Texas\extract_public_2018_20200216205325_damages_20180102-20180302Texas.csv"
#dbOps.upload_file(fp, conn, "maintenance_treatments")

#cname, res = dbOps.query("main_database","maintenance_treatments",conn)
# print(cname)
# print(res)

tab = dbOps.table_names("main_database",conn)
print(tab)