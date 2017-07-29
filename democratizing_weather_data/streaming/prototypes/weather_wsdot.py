import sys
import threading, logging, time
from kafka import KafkaProducer
#import pandas as pd
import requests

class FileProducer(threading.Thread):
    def __init__(self, topic_name, pairs):
        threading.Thread.__init__(self)
        self.topic_name = topic_name
        self.pairs = pairs

    daemon = True

    def run(self):
        print('About to create the weather_wsdot kafka producer')
        producer = KafkaProducer(bootstrap_servers = 'localhost:9092')

        """
        print('About to run a for loop over all our pairs: ', self.pairs)
        
        """
        producer.send(self.topic_name, str(self.pairs).encode('utf-8'))

def main():
    url_name, topic_name = sys.argv[1:]
    request = requests.get(url_name)
    response = request.json()

    print('About to call FileProducer')
    file_producer = FileProducer(topic_name, response)
    print('Calling file_producer.start()')
    file_producer.run()
    print('printing done')

if __name__ == "__main__":
    main()


