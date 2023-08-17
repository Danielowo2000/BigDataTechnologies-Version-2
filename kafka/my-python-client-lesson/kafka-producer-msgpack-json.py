import msgpack
import json
from kafka import KafkaProducer

# encode objects via msgpack. See https://msgpack.org/index.html
producer2 = KafkaProducer(value_serializer=msgpack.dumps)
producer2.send('msgpack-events', {'msgpack_key': 'msgpack_value'})
producer2.flush() # block until all async messages are sent

# produce json messages
producer3 = KafkaProducer(value_serializer=lambda m: json.dumps(m).encode('ascii'))
producer3.send('json-events', {'json_key': 'json_value'})
producer3.flush() # block until all async messages are sent

