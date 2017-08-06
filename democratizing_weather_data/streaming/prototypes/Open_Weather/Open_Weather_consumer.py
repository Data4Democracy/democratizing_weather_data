import json
import logging
import multiprocessing
import sys
import time
import kafka
from kafka import KafkaConsumer
#basefile_name = topic_name
#filename = 'weather.json'
message_id = 0
#full_filename = topic_name+filename
#print(full_filename)
class Consumer(multiprocessing.Process):
    def __init__(self, topic_name):
        self.topic_name = topic_name

    daemon = True
#    full_filename = 'weather.json'
#    full_filename = str(self.topic_name)+filename
 #   print(full_filename)

    def run(self):
        full_filename = 'weather.json'
        consumer = KafkaConsumer(bootstrap_servers='localhost:9092',
                                 auto_offset_reset='earliest')
        consumer.subscribe(self.topic_name)
        print(self.topic_name)

        for message in consumer:
        #if message == 'karan':
            print(message)
            print("=========-======================")
            payload1 = str(message.value)
#            payload ="%s" % (message.value)
            payload2 =str(message.value)
            payload = payload2[2:-1]
            
      
            print(payload)
            with open (full_filename,'w')as outputfile:
              #  json.dump(payload, outputfile)
                 outputfile.write(payload)
            with open ('badjason.json','w') as outfile1:
                json.dump(payload1,outfile1)
           # message_id=message_id+1



def main():
    topic_name = sys.argv[1]
    print(topic_name)
    consumer = Consumer(topic_name)
    consumer.run()
    print("we are about to sleep")
    time.sleep(10)


if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
        level=logging.INFO
    )
    main()
