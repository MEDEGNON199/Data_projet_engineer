import pandas as pd;
path_fil="data/tasks.json"
df=pd.read_json(path_fil)
print(df)