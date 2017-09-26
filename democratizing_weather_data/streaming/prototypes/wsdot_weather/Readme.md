# Running the Kafka Scripts
_work in progress.  needs moe info.

[TO DO]: describe how to acquire & setup a kafka server

[TO DO]: provide info on how to select the best producer/consumer script

Once on the kafka server ....
1. create a topic on server, for example:
    create topic :<wsdot_weather_test> usingn the following command line:
    ./kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic wsdot_weather_test

    You can check the topic list using:
    ./kafka-topics.sh --list --zookeeper localhost:2181

2. create a producer.py, and upload it to the server
    run the producer.py like:
    wsdot_weather_producer_server.py wsdot_weather_test "http://wsdot.wa.gov/Traffic/api/WeatherInformation/WeatherInformationREST.svc/GetCurrentWeatherInformationAsJson?AccessCode={<code you get from http://wsdot.com/traffic/api >}"

    'wsdot_weather_producer_server' is a one time running process
    'wsdot_weather_producer_server_every_minute' is running with interval period using buildin modules
    'wsdot_weather_producer_server_every_minute_v2' is running with interval period using extra module 'apscheduler'

3. create a consumer.py, and upload it to the server
    run the comsumer.py like:
    wsdot_weather_consumer_server_oldVersion.py wsdot_weather_test

4. test the pipeline

5. modify the consumer.py, run it locally
