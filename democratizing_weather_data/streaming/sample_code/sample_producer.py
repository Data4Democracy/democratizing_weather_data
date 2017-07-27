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
