import pandas as pd
from sklearn.preprocessing import OneHotEncoder


def createItemDictFromCSV():
    items = {}
    df = pd.read_csv("Products.csv")
    for index, row in df.iterrows():
        items[row['Name']] = Item(row['Name'], row['Price'], row['Description'], row['Link'], row['Disease'],  row['Item_id'])
    return items

def newItemToCSV(name, price, description, link, disease, item_id):
    df = pd.read_csv("Products.csv")
    df.loc[len(df)] = [name, price, description, link, disease, item_id]
    df.to_csv('Products.csv', index=False)

def delItemFromCSV(name):
    df = pd.read_csv("Products.csv")
    df = df.drop(df[df.Name == name].index)
    df.to_csv('Products.csv', index=False)

def generateIndexTable():
    indexToName = {}
    nameToIndex = {}
    df = pd.read_csv("Products.csv")
    for index, row in df.iterrows():
        indexToName[index] = row['Name']
        nameToIndex[row['Name']] = index

    return indexToName, nameToIndex
    

def generateOneHotEncoding():
    df = pd.read_csv("Products.csv")
    enc = preprocessing.OneHotEncoder()

    # 2. FIT
    enc.fit(df["disease"])

    # 3. Transform
    onehotlabels = enc.transform(X_2).toarray()
    onehotlabels.shape

    return indexToName, nameToIndex

class Item:
    def __init__(self, name, price, description, link, disease, item_id):
        self.name = name
        self.price = price
        self.description = description
        self.link = link
        self.disease = disease
        self.item_id = item_id
