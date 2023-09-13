import pandas as pd

data = {
    'nome' : ['João', 'Marta', 'Ary','Matheus', 'Michelle'],
    'idade' : [51, 37, 23,24, 33]
}

df = pd.DataFrame(data)

print(df[df['idade'] > 30])