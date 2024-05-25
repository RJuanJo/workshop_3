---

# Workshop 3 - Kafka Producer and Consumer

This project demonstrates a simple Kafka producer and consumer setup using Python. The producer script extracts data, sends it to a Kafka topic, and the consumer script consumes the data, performs some processing, and stores it in a MySQL database.

## Prerequisites

- Docker
- Docker Compose
- Python 3
- MySQL

## Credentials

The credentials for connecting to the MySQL database are stored in a JSON file named `credentials.json` located in the `config` directory. Ensure that the file contains the following fields:

```json
{
  "host": "your_host",
  "database": "your_database",
  "user": "your_user",
  "password": "your_password"
}
```
## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/RJuanJo/workshop_3.git
   ```

2. Navigate to the project directory:

   ```bash
   cd workshop_3
   ```

3. Requirements:
   Make sure you have all the necessary libraries for this project.
   
   Run the following command on a terminal shell in the root of the project:
   ```python
   pip install -r config/requirements.txt
   ```
4. Start the Docker containers:

   ```bash
   docker-compose up
   ```

5. Access the Kafka container:

   ```bash
   docker exec -it kafka_workshop bash
   ```

6. Create a Kafka topic:

   ```bash
   kafka-topics --bootstrap-server kafka_workshop:9092 --create --topic kafka_workshop3
   ```

7. Run the producer script:

   ```bash
   python producer.py
   ```

8. Run the consumer script:

   ```bash
   python consumer.py
   ```

## Usage

- The producer script (`producer.py`) extracts data and sends it to the Kafka topic `kafka_workshop3`.
- The consumer script (`consumer.py`) consumes the data from the Kafka topic, performs processing, and stores it in a MySQL database.
