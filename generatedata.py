import pandas as pd
import itemAPI

items = itemAPI.createItemDictFromCSV()

names = list(set(items.keys()))
diseases = set()
for item in items.values():
    diseases.add(item.disease)
diseases = list(diseases)
indexToName, nameToIndex = itemAPI.generateIndexTable()
data = []

for disease in diseases:
    for name in names:
        feature = []
        feature.append(nameToIndex[name])
        feature.append(disease)
        if items[name].disease == disease:
            feature.append(1)
        else:
            feature.append(0)
        data.append(feature)

print(data)
df = pd.DataFrame(data, columns = ['Name', 'Disease', 'Show'])


df.to_csv('data.csv', index=False)

    
