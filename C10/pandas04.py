from sklearn.datasets import load_iris
import pandas as pd

data = load_iris()
df = pd.DataFrame(data['data'], columns = data['feature_names'])
df['species'] = data['target']

print(df.head())
print('-' * 60)
print(df.plot())
print('-' * 60)
print(df.plot.scatter(x = 'sepal length (cm)', y = 'sepal width (cm)'))
print('-' * 60)

columns = ['sepal length (cm)', 'petal length (cm)', 'petal width (cm)', 'sepal width (cm)']

print(df[columns].plot.area())
print('-' * 60)

print(df.groupby('species').mean().plot.bar())
print('-' * 60)

print(df.groupby('species').count().plot.pie(y = 'sepal length (cm)'))