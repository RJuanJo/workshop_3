from kafka import KafkaProducer, KafkaConsumer
from json import dumps, loads
import pandas as pd

def kafka_producer():
    producer = KafkaProducer(
        value_serializer=lambda m: dumps(m).encode('utf-8'),
        bootstrap_servers = ['localhost:9092'],
    )
    return producer

def kafka_consumer():
    consumer = KafkaConsumer(
        'kafka_workshop3',
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group-1',
        value_deserializer=lambda m: loads(m.decode('utf-8')),
        bootstrap_servers=['localhost:9092']
        )
    return consumer