import sys
import logging
import multiprocessing
import json
import time

from kafka import KafkaConsumer

basefile_name = topic_name
filename = 'weather.json'
message_id = 0
full_filename = basefile_name+filename
print(full_filename)
class Consumer(multiprocessing.Process):
    def __init__(self, topic_name):
        self.topic_name = topic_name

    daemon = True

    def run(self):
        consumer = KafkaConsumer(bootstrap_servers='localhost:9092',
                                 auto_offset_reset='earliest')
        consumer.subscribe(self.topic_name)

      for message in consumer:
        #if message == 'karan':
            print (message)
            with open (full_filename,'w')as outputfile
            json.dump(message, outputfile)
            message_id=message_id+1



def main():
    topic_name = sys.argv[1:]
    consumer = Consumer(topic_name)
    consumer.run()
    time.sleep(10)


if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
        level=logging.INFO
    )
    main()