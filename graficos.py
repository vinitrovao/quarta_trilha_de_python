import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("mt.cars.csv", index_col=0)
print(df)


print(df.head())

print(df.info())

print(df.describe())

sns.set_theme(style="whitegrid")

plt.figure(figsize=(10, 6))
sns.scatterplot(x='hp', y='mpg', data=df)
for car, mpg, hp in zip(df.index, df['mpg'], df['hp']):
    plt.text(hp, mpg, car, fontsize=9, ha='left')
plt.title('Milhas por Galão vs Cavalos de Potência')
plt.xlabel('Cavalos de Potência (hp)')
plt.ylabel('Milhas por Galão (mpg)')
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(df['mpg'], bins=10, kde=True)
plt.title('Distribuição de Milhas por Galão')
plt.xlabel('Milhas por Galão (mpg)')
plt.ylabel('Frequência')
plt.show()


plt.figure(figsize=(10, 6))
sns.countplot(x='cyl', data=df)
plt.title('Quantidade de Carros por Número de Cilindros')
plt.xlabel('Número de Cilindros')
plt.ylabel('Quantidade de Carros')
plt.show()
