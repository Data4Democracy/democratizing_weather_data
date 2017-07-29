import sys   
import threading, logging, time
from kafka import KafkaProducer
import pandas as pd


class FileProducer(threading.Thread):

    def __init__(self, topic_name, pairs):
        threading.Thread.__init__(self)
        self.topic_name = topic_name
        self.pairs = pairs

    daemon = True

    def run(self):
        print('About to create our kafka producer')
        producer = KafkaProducer(bootstrap_servers='localhost:9092')

        print('About to run a for loop over all our pairs: ' , self.pairs)
        for p in self.pairs:
            print('Now sending to the topic ' , self.topic_name , ' the message ' , p)
            producer.send(self.topic_name, str(p).encode('utf-8'))
            time.sleep(1)

def main():
    file_name, column_name, topic_name = sys.argv[1:]
    bellevue = pd.read_csv(file_name)
    print("stl_min colujmn: " , list(bellevue[column_name]))
    pairs = list(bellevue[column_name])

    print('About to call FileProducer')
    file_producer = FileProducer(topic_name, pairs)
    print('Calling file_producer.start()')
    file_producer.run()
    print('printing done')

if __name__ == "__main__":
    main()



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