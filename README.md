docker-compose up
docker exec -it kafka_workshop bash
kafka-topics --bootstrap-server kafka_workshop:9092 --create --topic kafka_workshop3
python producer.py
python consumer.py