import pandas as pd
import numpy


def createDocDictFromCSV():
    items = {}
    df = pd.read_csv("Doctors.csv")
    for index, row in df.iterrows():
        items[row['Name']] = Doc(row['Name'], row['Rating'], row['Link'], row['Specialty'], row['Contact'])
    return items


class Doc:
    def __init__(self, name, rating, link, specialty, contact):
        self.name = name
        self.rating = rating
        self.link = link
        self.specialty = specialty
        self.contact = contact
