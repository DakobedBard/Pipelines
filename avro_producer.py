from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer
import time


value_schema_str = """
{
   "namespace": "hellokoding.kafka",
   "name": "value",
   "type": "record",
   "fields" : [
     {"name" : "username", "type" : "string"},
     {"name" : "tweet", "type" : "string"},
     {"name" : "location", "type" : "string"}
   ]
}
"""

key_schema_str = """
{
   "namespace": "hellokoding.kafka",
   "name": "key",
   "type": "record",
   "fields" : [
     {"name" : "tweetID", "type" : "int"}
   ]
}
"""

value_schema = avro.loads(value_schema_str)
key_schema = avro.loads(key_schema_str)
value = {"username": "BernieBro", "tweet": "Bernie is the champ", "location":"Seattle"}
key = {"tweetID": 1}

avroProducer = AvroProducer({
    'bootstrap.servers': 'localhost:9092',
    'schema.registry.url': 'http://localhost:8081'
    }, default_key_schema=key_schema, default_value_schema=value_schema)

avroProducer.produce(topic='kafkatweetss', value=value, key=key)
avroProducer.flush()
