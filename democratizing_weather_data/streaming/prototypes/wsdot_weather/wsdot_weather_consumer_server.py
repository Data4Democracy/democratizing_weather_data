import sys
import logging
import multiprocessing
import json
import time

from kafka import KafkaConsumer


class Consumer (multiprocessing.Process):
    def __init__(self, topic_name):
        self.topic_name = topic_name

    daemon = True

    def run(self):
        consumer = KafkaConsumer(bootstrap_servers = 'localhost:9092',
                                 auto_offset_reset = 'latest')
        consumer.subscribe(self.topic_name)

        for message in consumer:
            print (message.value.decode('utf-8'))
            with open('test_store_consumer_wsdot.json', 'w') as outfile:
                outfile.write(message.value.decode('utf-8'))


def main():
    topic_name = sys.argv[1:]
    consumer = Consumer(topic_name)
    consumer.run()
    time.sleep(10)

if __name__ == "__main__":
    logging.basicConfig(
        format = '%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
        level = logging.INFO
    )
    main()