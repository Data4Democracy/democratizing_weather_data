import sys
from kafka import KafkaClient, SimpleProducer
import json,requests

topic = sys.argv[1]
kafka = KafkaClient('localhost:9092')

producer = SimpleProducer(kafka)

#url= 'http://countdown.api.tfl.gov.uk/interfaces/ura/instant_V1'
url = sys.argv[2]
r = requests.get(url,stream=True)

for line in r.iter_lines():
	producer.send_messages(topic,line)
	print(line)

kafka.close()
