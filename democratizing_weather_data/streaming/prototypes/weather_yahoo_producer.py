import sys   
import threading, logging, time
import json
import urllib
from kafka import KafkaProducer
import pandas as pd
from pandas.io.json import json_normalize

class FileProducer(threading.Thread):

    def __init__(self, topic_name, pairs):
        threading.Thread.__init__(self)
        self.topic_name = topic_name
        self.normal_json = normal_json

    daemon = True

    def run(self):
        print('About to create our kafka producer')
        producer = KafkaProducer(bootstrap_servers='localhost:9092')

        print('About to send the json file: ' , self.normal_json)
      

        """
        print('About to run a for loop over all our pairs: ' , self.pairs)
        for p in self.pairs:
            print('Now sending to the topic ' , self.topic_name , ' the message ' , p)
            producer.send(self.topic_name, str(p).encode('utf-8'))
            time.sleep(1)
        """

def main():
    #TODO make url an argument isntead of hard-coded.

    topic_name = sys.argv[1:]

    """
    file_name, column_name, topic_name = sys.argv[1:]
    bellevue = pd.read_csv(file_name)
    print("stl_min colujmn: " , list(bellevue[column_name]))
    pairs = list(bellevue[column_name])
    """
    #woeid 2502265 is for Sunnyvale CA. Replace this ID with any other ID for other weather forecasts.
    #Find other IDs on http://www.woeidlookup.com/
    url = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%3D2502265&format=json&diagnostics=true&callback=' 
    # select * from weather.forecast where woeid %3D 2502265 & format=json & diagnostics=true & callback=' 


    url_obj = urllib.urlopen(url)
    raw_json = json.load(url_obj)
    normal_json = json_normalize(raw_json['query']['results']['channel']) 

    print('About to call FileProducer')
    file_producer = FileProducer(topic_name, normal_json)
    print('Calling file_producer.start()')
    file_producer.run()
    print('printing done')

if __name__ == "__main__":
    main()