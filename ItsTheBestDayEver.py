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
dataset = pd.read_csv('LipfordDatasetUpdated.csv')

#read only quantitative data in (needs to change to fit one hot in
quantdataset = dataset.select_dtypes(include=[float])
quantdataset.shape
quantdataset.isnull().sum()
quantdataset = quantdataset.fillna(quantdataset.mean())
#print(quantdataset)

onehotdataset = dataset.select_dtypes(include=[object])
onehotdataset = onehotdataset.fillna('None')
onehotdataset.shape
onehotdataset2 = onehotdataset.drop('exit_desc', axis =1)
print(onehotdataset)
#print(onehotdataset2)

""" Convert to one Hot """
enc = OneHotEncoder(handle_unknown = 'ignore')
onehot = pd.DataFrame(enc.fit_transform(onehotdataset).toarray())
#print(onehot)


""" Scaling the Features """
scaler = StandardScaler()
scaler.fit(quantdataset)
scaled_quant = scaler.transform(quantdataset)
modified_quant = pd.DataFrame(scaled_quant)
print(modified_quant)

""" Merge """
alldata = pd.concat([modified_quant, onehot], axis = 1)
print(alldata)


""" Create Train Test """
X_train, X_test, y_train, y_test = train_test_split(alldata, onehotdataset['exit_desc'], test_size = 0.25)
print(X_train)
print(y_train)


""" Deciding K neighbors """
knn = KNeighborsClassifier(n_neighbors = 8)

knn.fit(X_train, y_train)
#pickle to write object to file
pred = knn.predict(X_test) #gets the prediction using the classifier
#print(knn.score(X_test, y_test))


""" Confusion matrix """
from sklearn.metrics import classification_report, confusion_matrix

print(confusion_matrix(y_test, pred))
print('\n')
print(classification_report(y_test, pred)) #This is the accuracy, avg, weight avg report


""" Choosing a K-value and creating visualization of Error Rate """
error_rate = []

for i in range(1, 35):
    #print(y_test.shape)
    knn = KNeighborsClassifier(n_neighbors = i)
    knn.fit(X_train, y_train)
    pred_i = knn.predict(X_test)
    #print(pred_i[pred_i!= y_test])
    #print(y_test)
    error_rate.append(np.mean(pred_i != y_test))
#print(error_rate)

plt.figure(figsize=(10,6))
plt.plot(range(1,35), 1-np.array(error_rate), color = 'blue',
                 linestyle ='dashed', marker = 'o',
         markerfacecolor = 'blue', markersize = 10)
"""

plt.plot(range(1,35), error_rate, color = 'blue',
                 linestyle ='dashed', marker = 'o',
         markerfacecolor = 'blue', markersize = 10)
"""


plt.title('Error vs K Value')
plt.xlabel('K')
print("Done with program")
plt.ylabel('Error Rate')
plt.show()




