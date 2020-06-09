from requests import request
import json
import pandas
from pandas.io.json import json_normalize
import numpy 


#list URLS to be fetched 
url = "https://services.arcgis.com/KTcxiTD9dsQw4r7Z/arcgis/rest/services/TxDOT_AADT_Annuals/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json"
content = request(url=url,method='get')
dict = content.json()
df = json_normalize(dict['features'])
print(df)
