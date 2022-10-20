import pandas as pd

arquivo = r"C:\Users\leonardo.simoes\OneDrive - Sistema FIEB\salarios.csv"
df = pd.read_csv(arquivo)

print(df.head())
