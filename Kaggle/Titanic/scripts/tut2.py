import pandas as pd
import pylab as pylab
import numpy as np

# Table = DataFrame
# Column = Series
# Row = ???

df = pd.read_csv('../data/train.csv', header=0)
#df.head(3)
#df.info()
#df.dtypes
#df.describe()
#df['Age'][0:10]
#df.Age[0:10]
#df['Age']
#df.Age
#df.Age.mean()
#df[['Sex','Pclass','Age']]
#df['Age'] > 20
#df[df['Age'] > 60]
#df[df['Age'] > 60][['Sex', 'Pclass', 'Age', 'Survived']]
#df[df['Age'].isnull()][['Sex', 'Pclass', 'Age']]
#for i in range(1,4):
#    print i, len(df[(df.Sex == 'male') & (df.Pclass == i) ])
#df.Age.hist()
#pylab.show()
###df['Age'].dropna().hist(bins=16, range=(0,80), alpha = .5)
#pylab.show()

#Creating new column (male to M, female to F)
#df['Gender'] = df['Sex'].map(lambda x: x[0].upper())
df['Gender'] = df['Sex'].map({'female':0,'male':1}).astype(int)
#df['PlaceEmbarked'] = df['Embarked'].dropna().map({'S':0,'C':1,'Q':2}).astype(int) ??? problem with nulls

print(df.head(20))











#print (df[df.notnull()])


