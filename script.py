import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('base_vendas_projeto1.xlsx')

is_null = df.isnull().sum()  # Confirma se há dados invalidos
# print(noValue)
df.drop_duplicates() # Exclui valores duplicados
# print(is_dupli)
df = df.dropna()  # Remove valores  nulos

# Garante que a coluna 'Data' esta definida como Data
df['Data'] = pd.to_datetime(df['Data'])
# Calcula a receita obtida dos pprodutos
df['Receita'] = df['Quantidade'] * df['Preço Unitário']
df['Lucro'] = df['Receita'] - df['Custo Unitário']  # Calcula o lucro

regiao_filtrada = df.loc[df['Região'] == 'Nordeste', ['Produto', 'Lucro']] # Filtra por toda a região nordeste e mostra o produto e o lucro
lucro_filtrado = df[df['Lucro'] < 500] # Filtra lucros menores que 500

# Receita total por produto
print(df.groupby('Produto')['Receita'].sum().sort_values(ascending=False))

# Receita mensal
df['AnoMes'] = df['Data'].dt.to_period('M')
print(df.groupby('AnoMes')['Receita'].sum())

# Lucro médio por vendedor
print(df.groupby('Vendedor')['Lucro'].mean().sort_values(ascending=False))


df.to_excel('vendas_tratadas.xlsx', index=False)
print("Base de dados tradada com sucesso!")

df.groupby('Produto')['Receita'].sum().plot(kind='bar', title='Receita por Produto')
plt.ylabel('Receita total')
plt.tight_layout()
# plt.show()
