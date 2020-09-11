# import sys
# import scipy
import sklearn
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report,accuracy_score
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
import pickle

data = pd.read_csv("credit_card.csv")
#print(data.columns)
Fraud=data[data["Class"]==1]
Valid=data[data["Class"]==0]

outlier_fraction=float(len(Fraud ))/float(len(Valid))
#print(outlier_fraction)
#print('Fraud Cases: {}'.format(len(data[data['Class'] == 1])))
#print('Valid Transactions: {}'.format(len(data[data['Class'] == 0])))

corrmat = data.corr()
fig = plt.figure(figsize=(10,10))
ax = sns.heatmap(corrmat,vmax=0.8,square=True)

#plt.show()
# Get all the columns from the dataFrame
columns = data.columns.tolist()

# Filter the columns to remove data we do not want
columns = [c for c in columns if c not in ["Class"]]

# Store the variable we'll be predicting on
target = "Class"
X = data[columns]
Y = data[target]    
# Print shapes
#print(X.shape)
#print(Y.shape)
# define random states
state = 1

# define outlier detection tools to be compared
clf = IsolationForest(max_samples = len(X), contamination = outlier_fraction, random_state = state, behaviour = 'new')
n_outliers = len(Fraud)

clf.fit(X)
pickle.dump(clf, open('model.pkl','wb'))