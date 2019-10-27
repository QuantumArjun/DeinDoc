import pandas as pd
import numpy


def createDocDictFromCSV():
    items = {}
    df = pd.read_csv("Doctors.csv")
    for index, row in df.iterrows():
        items[row['Name']] = Doc(row['Name'], row['Rating'], row['Link'], row['Specialty'], row['Contact'], row['Doc_id'])
    return items

def createDocIDDictFromCSV():
    items = {}
    df = pd.read_csv("Doctors.csv")
    for index, row in df.iterrows():
        items[row['Doc_id']] = Doc(row['Name'], row['Rating'], row['Link'], row['Specialty'], row['Contact'], row['Doc_id'])
    return items


class Doc:
    def __init__(self, name, rating, link, specialty, contact,doc_id):
        self.name = name
        self.rating = rating
        self.link = link
        self.specialty = specialty
        self.contact = contact
        self.doc_id = doc_id
