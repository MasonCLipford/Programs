import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import csv

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn import svm, datasets
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
from sklearn.preprocessing import label_binarize
from sklearn.metrics import average_precision_score
from sklearn.preprocessing import OneHotEncoder

random_state = np.random.RandomState(0)
dataset = pd.read_csv('DatasetB.csv')
onehotdataset = pd.read_csv('LipfordDatasetUpdated.csv')

#read only quantitative data in (needs to change to fit one hot in
dataset.shape
dataset.isnull().sum()
print(dataset.head())

""" Filling the null values """
modifiedDataset = dataset.fillna(dataset.mean())


""" Check for null values """
onehotdataset = onehotdataset.select_dtypes(include=[object])
onehotdataset = onehotdataset.fillna('None')
onehotdataset.shape
print(onehotdataset.head(10))

""" Take out 'exit_desc' """ #trying to pull out exit_desc before we convert to one hot
#scaler = StandardScaler()
#scaler.fit(onehotdataset.drop('exit_desc', axis = 1)) #taking this out of the categorical rather than quant

""" creating instance of one-hot-encoder """
enc = OneHotEncoder(handle_unknown = 'ignore')

""" passing one hot encoded columns """ 
enc_df = pd.DataFrame(enc.fit_transform(onehotdataset).toarray())
print(enc_df)

""" Standardize/Scaling the Variables """
scaler = StandardScaler()
scaler.fit(modifiedDataset.drop('exit_desc', axis = 1))#these two lines need to go before 
scaled_features = scaler.transform(modifiedDataset.drop('exit_desc', axis = 1))##
#uses alldata
#doesn't drop 'exit_desc'
modifiedDataset_features = pd.DataFrame(scaled_features, columns = modifiedDataset.columns[:-1])
print(modifiedDataset_features.head())

""" One Hot Encoding """
#pull in one hot encoding
#push onto modified dataset
#How do I know what one hot is doing, how does it understand when it's only numbers as what relates to what
alldata = pd.concat([modifiedDataset_features, enc_df], axis = 1)
print(alldata.head())




""" Creating a Train and Test Split using KNN model """
X_train, X_test, y_train, y_test = train_test_split(alldata, modifiedDataset['exit_desc'], test_size = 0.30)


""" Deciding K neighbors """
knn = KNeighborsClassifier(n_neighbors = 7)
knn.fit(X_train, y_train)
pred = knn.predict(X_test) #gets the prediction using the classifier
print(knn.score(X_test, y_test))


""" Confusion matrix """
from sklearn.metrics import classification_report, confusion_matrix

print(confusion_matrix(y_test, pred))
print('\n')
print(classification_report(y_test, pred)) #This is the accuracy, avg, weight avg report


""" Choosing a K-value and creating visualization or Error Rate """
error_rate = []

for i in range(1, 20):
    knn = KNeighborsClassifier(n_neighbors = i)
    knn.fit(X_train, y_train)
    pred_i = knn.predict(X_test)
    error_rate.append(np.mean(pred_i != y_test))

plt.figure(figsize=(10,6))
plt.plot(range(1,20), error_rate, color = 'blue',
                 linestyle ='dashed', marker = 'o',
         markerfacecolor = 'blue', markersize = 10)

plt.title('Error Rate vs K Value')
plt.xlabel('K')
print("Done with program")
plt.ylabel('Error Rate')
plt.show()
