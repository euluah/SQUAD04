import pandas as pd

data = {
    'nome' : ['João', 'Marta', 'Ary','Matheus', 'Michelle', 'Luana'],
    'idade' : [51, 37, 23,24, 33, 24],
    'cidade': ['Recife', 'Recife', 'Recife', 'Salvador', 'São Paulo', 'Manaus']
}

df = pd.DataFrame(data)

print(df[df['cidade'] == 'Recife'])
