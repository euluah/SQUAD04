from faker import Faker
import random

faker = Faker('pt_br')

data = {
    "Nome": [faker.name(), faker.name()],
    "Cidade": [faker.address(), faker.name()],
    "Idade":[random.randint(1,100)]
}

print(data)