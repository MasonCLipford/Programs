import numpy as np
import pandas as pd

#from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

#encoding = 'ISO-8859-1'

dataset = pd.read_csv('LipfordDatasetUpdated.csv')#read in the csv

""" Check for null values """
dataset = dataset.select_dtypes(include=[object])#limit the categorical data using df.select-dtypes()
dataset = dataset.fillna('None') #temporary fix for empty values
dataset.shape
print(dataset.head(10))

""" creating instance of one-hot-encoder """
enc = OneHotEncoder(handle_unknown = 'ignore')

""" passing ... columns """ #label encoded values of qualitative data
enc_df = pd.DataFrame(enc.fit_transform(dataset).toarray())
print(enc_df)
