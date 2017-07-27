This is a collecton of sample code to assist with developming streaming capabilities for democratizing_weather_data

| file | description |
|-----:|-------------|
|sample_consumer.py | kafka consumer implemented in python|
|sample_producer.py | kafka producer implemented in python|
|seatgeek_query.py |  using a web api to pull json data and store as csv|
|yahoo_weather.py | using a web api to pull json data, normalize, store as csv|
|spark_processor.py | spark in python (not sure we'll need this)|

Cool-looking table, huh?  I learned how to do it from [adam-p's markdown cheat sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

Suggested Way forward
- Combine front-half yahoo_weather.py and sample_producer.py in such a way that the weather json is retreived via API, then the whole json document is sent as a kafka message.
- Combine the back-half of yahoo_weather.py with sample_consumer.py, in such a way that when the kafka message is received, the json is pulled out, normalized, and saved as csv.
