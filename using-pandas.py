#Get App, Category, Rating and Price from the first 21 lines of the document

import pandas as pd

df = pd.read_csv('data/googleplaystore.csv')
req_columns = ['App', 'Category', 'Rating', 'Price']
df = df[req_columns]
print ("Shape of dataset: ", df.shape)
df.head(21)