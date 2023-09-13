from GPTQueryEngine import GPTQueryEngine
import random
import pandas as pd

#toma noticia random de un csv
csv_file = "noticias-2023-05-31.csv"
data = pd.read_csv(csv_file)
random_index = random.randint(0, data.shape[0] - 1)
new = data['text'][random_index]
print("Random Index:",random_index)

#test GPTQueryEngine (no abusar consume plata xd)
query_engine = GPTQueryEngine()
result = query_engine.query(new)
print(result)
for item in result['data']:
    print(item['location'])
