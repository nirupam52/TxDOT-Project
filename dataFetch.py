from requests import request
import json
import pandas
from pandas.io.json import json_normalize
import numpy 

class DataFetch:

    def fetch(url):
        content = request(url=url,method='get')
        dict = content.json()
        df = json_normalize(dict['features'])
        return df 
