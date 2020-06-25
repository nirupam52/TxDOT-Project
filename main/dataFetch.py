from requests import request
import json
import pandas
from arcgis.gis import GIS
from arcgis.features import FeatureLayerCollection
from IPython.display import display
from pandas.io.json import json_normalize
import numpy 

gis = GIS()

class DataFetch:

    def fetch(title):
        search_results = gis.content.search('title: {}'.format(title), 'Feature Layer')
        print(*list(enumerate(search_results)), sep='\n')
        choice = int(input("enter the index of the result you want \n"))
        url = search_results[choice].layers[0]
        result = url.query( out_fields='*')
        df = result.sdf
        return df
