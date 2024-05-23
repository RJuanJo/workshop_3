from services.kafka import kafka_producer
from services.functions import extract_and_combine_data

data = extract_and_combine_data()
producer = kafka_producer()
for index in range(len(data)):
    producer.send("kafka_workshop3", value=data.iloc[index].to_dict())
producer.send("kafka_workshop3", value={'proccess':0})
print("message sent")
