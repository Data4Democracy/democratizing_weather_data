from __future__ import print_function

import re
import sys

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: kafka_wordcount.py <zk> <topic>", file=sys.stderr)
        exit(-1)

    sc = SparkContext(appName="LondonStream")
    ssc = StreamingContext(sc, 1)

    def nameFilter(word):
        pattern = re.compile('^[A-Z][0-9]+$')
        match = pattern.match(word)
        if match:
            return True
        else:
            return False

    zkQuorum, topic = sys.argv[1:]
    kvs = KafkaUtils.createStream(ssc, zkQuorum, "spark-streaming-consumer", {topic: 1})
    lines = kvs.map(lambda x: x[1])
    counts = lines.flatMap(lambda line: line.replace("[", "").replace("]", "").replace('"',"").split(",")) \
        .filter(nameFilter) \
        .map(lambda line:  (line, 1)) \
        .reduceByKey(lambda a, b: a+b)
    counts.pprint()

    ssc.start()
    ssc.awaitTermination()
