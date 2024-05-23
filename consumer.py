from services.kafka import kafka_consumer
import pandas as pd
import joblib

consumer = kafka_consumer()
model = 'model/random_forest_model.pkl'

data = pd.DataFrame(columns=['Country', 'Region', 'Happiness_Rank', 'Happiness_Score',
       'Economy_GDP_per_Capita', 'Family', 'Health_Life_Expectancy', 'Freedom',
       'Trust_Government_Corruption', 'Generosity', 'Year'])
for m in consumer:
    print(m.value)
    if m.value == "{'proccess': 0}":
        break
    data.loc[len(data)] = m.value

model_reading = joblib.load(model)
data['PredictedHapiness']=model_reading(['Economy_GDP_per_Capita', 'Family', 'Health_Life_Expectancy', 
                  'Freedom', 'Trust_Government_Corruption', 'Generosity', 'Year'])