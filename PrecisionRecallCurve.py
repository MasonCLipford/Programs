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
from sklearn.datasets import make_classification
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score

data = pd.read_csv('DatasetB.csv')
dataset = data.fillna('0')

X = dataset.drop(columns=['exit_desc'])
y = dataset['exit_desc'].values

""" Train and Test set """
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
knn = KNeighborsClassifier(n_neighbors = 7)
knn.fit(X_train, y_train)
knn.predict(X_test)[0:10]
knn.score(X_test, y_test)

#Error is somehwere in predicting probability 
""" Predicting prbability with X_test and FPR, TPR """
y_scores = knn.predict_proba(X_test)
fpr, tpr, threshold = roc_curve(y_test, y_scores[:, 1])
#false positive rate and true positive rate
roc_auc = auc(fpr, tpr)


""" Python func to plot ROC curve """
plt.plot(fpr, tpr, 'b', label='AUC = %0.2f' % roc_auc)
plt.legen(loc = 'lower right')
plt.plot([0, 1], [0, 1], 'r--')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.show()
