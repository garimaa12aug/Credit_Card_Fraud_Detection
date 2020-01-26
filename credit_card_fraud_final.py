# -*- coding: utf-8 -*-
"""Credit_Card_Fraud_Final.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QB7BD_N5toEtxTysfA8G-ejuCkdQUDga
"""

import numpy as np
import pandas as pd
import keras
from keras import layers
from keras import Sequential
import sklearn
from sklearn.model_selection import train_test_split

# Load the dataset from the csv file using pandas
data = pd.read_csv('creditcard.csv')


print(data.shape)
print(data.describe())
data = data.sample(frac=0.1)
print(data.shape)
print(data.describe())

# Plot histograms of each parameter 
data.hist(figsize = (20, 20))
plt.show()

# Determine number of fraud cases in dataset
Fraud = data[data['Class'] == 1]
Valid = data[data['Class'] == 0]
print("Number of fraudlent transactions are" ,len(Fraud))
print("Number of valid transactions are" ,len(Valid))

columns = data.columns.to_list()
columns = [c for c in columns if c not in ["Class"]]
target = "Class"
X = data[columns]
Y = data[target]

X_train, X_test, y_train, y_test = train_test_split(X , Y, test_size=0.2, shuffle=False, stratify= None)

print('X_train Shape = ',X_train.shape)
print('Y_train Shape= ', y_train.shape)
print('X_Test Shape = ', X_test.shape)
print('Y_test Shape =', y_test.shape)

#*************************Using Logistic Regression**********************************************
from sklearn.linear_model import LogisticRegression
clg = LogisticRegression()
clg.fit(X_train, y_train)
clg.predict(X_test)
print(clg.score(X_test,y_test))

#*******************************Using neural networks*************************************************
from keras import models
network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape = (30,) ))
network.add(layers.Dense(256,activation = 'relu'))
network.add(layers.Dense(32,activation = 'relu'))
network.add(layers.Dense(8,activation = 'relu'))
network.add(layers.Dense(1,activation = 'sigmoid'))
network.compile(optimizer = 'rmsprop', loss = 'binary_crossentropy',metrics = ['accuracy'])
network.fit(X_train,y_train , epochs = 10, batch_size = 512)

test_loss , test_acc = network.evaluate(X_test , y_test)
print(test_acc)
print(test_loss)

testing = network.predict(X_test)
print(testing.shape)
print(testing[:10])

print(X_test[:10])

print(y_test[:10])