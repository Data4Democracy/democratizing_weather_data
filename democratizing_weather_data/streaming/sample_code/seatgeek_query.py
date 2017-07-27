import os # can probably ignore/comment this out.
import datetime # can probably ignore/comment this out.
import json
import urllib
import pandas as pd
from pandas.io.json import json_normalize


def seatgeek_query(key, secret, argument_dict={}):
    argument_dict.update({'client_id': key, 'client_secret': secret})
    query = urllib.urlencode(argument_dict)
    endpoint = 'http://api.seatgeek.com/2/events?'
    url = endpoint+query
    url_object = urllib.urlopen(url)
    
    sg = {'defaultKey': 'defaultValue'}
    try:
        sg = json.load(url_object)
    except ValueError:
        print 'Invalid url_object returned for url:' + url
    return sg
    
#key = 'your key here'
#secret = 'your secret here'


sg = seatgeek_query(key, secret, {'postal_code': 98122, 'per_page': 100})
if 'events' in sg.keys():
    sg_df = json_normalize(sg['events'])
sg_df.to_csv('seatgeek_query.csv', sep=',')