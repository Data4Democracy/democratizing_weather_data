from __future__ import print_function

import sys

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: kafka_wordcount.py <zk> <topic>", file=sys.stderr)
        exit(-1)

    sc = SparkContext(appName="PythonStreamingKafka")
    ssc = StreamingContext(sc, 1)

    zkQuorum, topic = sys.argv[1:]
    kvs = KafkaUtils.createStream(ssc, zkQuorum, "spark-streaming-consumer", {topic: 1})

    def savetofile(rdd):
        rdd.foreach(lambda rec: open("/.output_file.csv", "a").write(
            str(rec),"\n"))

    lines = kvs.map(lambda x: x[1])
    threshold = lines.map(lambda x: 0 if x > 33 else 1)
    threshold.foreachRDD(savetofile)
    threshold.pprint()

    ssc.start()
    ssc.awaitTermination()


# /opt/spark/spark-2.1.1-bin-hadoop2.7/bin/spark-submit \
    # --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.0.2 \
    # spark_processor.py localhost:2181 weather_testing


