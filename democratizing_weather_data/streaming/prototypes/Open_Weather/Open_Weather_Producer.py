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
        self.pairs  = pairs

    daemon = True

    def run(self):
        print('About to create our kafka producer')
        producer = KafkaProducer(bootstrap_servers='localhost:9092')
        time.sleep(10)
        producer.send(self.topic_name, str(self.pairs).encode('utf-8'))

        #print('About to send the json file: ' , self.normal_json)
      

        """
        print('About to run a for loop over all our pairs: ' , self.pairs)
        for p in self.pairs:
            print('Now sending to the topic ' , self.topic_name , ' the message ' , p)
            producer.send(self.topic_name, str(p).encode('utf-8'))
            time.sleep(1)
        """

def main():
    #TODO make url an argument isntead of hard-coded
    #below sample url and api key for testing
    #http://samples.openweathermap.org/data/2.5/weather?zip=98005,us&appid=
    #api_key=b1b15e88fa797225412429c1c50c122a1
    #url = "http://samples.openweathermap.org/data/2.5/weather?lat=35&lon=139&appid="+ api_key
    url_name, api_key, topic_name, = sys.argv[1:]
    final_url = url_name + api_key
    print(final_url)
    request = requests.get(final_url)
    response = request.json()

    
    print('About to call FileProducer')
    file_producer = FileProducer(topic_name, response)
    print('Calling file_producer.start()')
    file_producer.run()
    print('printing done')

if __name__ == "__main__":
    main()