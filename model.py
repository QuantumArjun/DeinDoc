import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import GridSearchCV

import pickle
import itemAPI
indexToName, nameToIndex = itemAPI.generateIndexTable()

df = pd.read_csv("data.csv")

def lookup(x):
    oneHotLookup = itemAPI.generateOneHotTable()
    return oneHotLookup[x]
df["Disease"] = df["Disease"].apply(lambda x: lookup(x))

x = df[['Name', 'Disease']]
y = df['Show']

clf = MLPClassifier(activation='logistic', hidden_layer_sizes=(18,), solver='lbfgs')
clf.fit(x, y)
for i in range(1, 27):
    data = [[i, 1]]
    test = pd.DataFrame(data, columns = ['Name', 'Disease'])

    if (clf.predict_proba(test)[0][1] > .17):
        print(indexToName[i])
filename = 'model.sav'
pickle.dump(clf, open(filename, 'wb'))


