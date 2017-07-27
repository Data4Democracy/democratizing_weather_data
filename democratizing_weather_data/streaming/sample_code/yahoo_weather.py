import json
import urllib
import pandas as pd
from pandas.io.json import json_normalize

#woeid 2502265 is for Sunnyvale CA. Replace this ID with any other ID for other weather forecasts.
#Find other IDs on http://www.woeidlookup.com/
url = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%3D2502265&format=json&diagnostics=true&callback=' 
# select * from weather.forecast where woeid %3D 2502265 & format=json & diagnostics=true & callback=' 


url_obj = urllib.urlopen(url)
x = json.load(url_obj)
y = json_normalize(x['query']['results']['channel']) 

y.to_csv('yahoo_weather.csv', sep=',') # end result needs a bit more normalization.