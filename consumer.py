from services.kafka import kafka_consumer
import pandas as pd
import joblib
from sqlalchemy import create_engine
import time
import json

model_path = 'model/random_forest_model.pkl'
model = joblib.load(model_path)
consumer = kafka_consumer()

def connect_to_database():
    with open('config/credentials.json', 'r') as f:
        credentials = json.load(f)
    
    connection_string = f"mysql+pymysql://{credentials['user']}:{credentials['password']}@{credentials['host']}/{credentials['database']}"
    engine = create_engine(connection_string)
    return engine

def process_and_store_data(message, engine, model):
    data = pd.DataFrame([message.value])
    data['PredictedHappiness'] = model.predict(data[['Economy_GDP_per_Capita', 'Family', 'Health_Life_Expectancy', 
                                                      'Freedom', 'Trust_Government_Corruption', 'Generosity', 'Year']])
    data.to_sql('prediction', con=engine, if_exists='append', index=False)

def main():
    engine = connect_to_database()
    for message in consumer:
        print(message.value)
        if message.value == {'proccess': 0}:
            break
        process_and_store_data(message, engine, model)
        time.sleep(2) 

if __name__ == "__main__":
    main()
