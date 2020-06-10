from dataFetch import DataFetch 

dat = DataFetch.fetch("https://services.arcgis.com/KTcxiTD9dsQw4r7Z/arcgis/rest/services/TxDOT_AADT_Annuals/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json")
print(dat)