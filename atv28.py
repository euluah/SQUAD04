import pandas as pd
from faker import Faker
import random

faker = Faker('pt_br')

data = {
    "Nome": [faker.name()],
    "Cidade": [faker.address()],
    "Idade":[random.randint(1,100)],
}


df = pd.DataFrame(data)
print(df)
df.to_csv("minhaprimeiratabela.csv")