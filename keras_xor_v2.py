# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 09:28:37 2018

@author: Mauro_Sergio
"""
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense

entrada = pd.read_csv('inputXOR.csv')
saida = pd.read_csv('outputXOR.csv')

x = entrada[:600]
y = saida[:600]

print (x,y)


model = Sequential()
model.add(Dense(10, input_dim = 3 , activation = 'relu'))
model.add(Dense(6, activation = 'relu'))
model.add(Dense(1,activation = 'sigmoid'))

model.compile(loss = 'mean_squared_error', optimizer = 'adam', metrics = ['accuracy'])
model.fit(x , y, epochs=500, batch_size = 1)

pred = entrada[600:]
model.predict(pred)
