# -*- coding: utf-8 -*-
"""bostonHousing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CO54jNz0He0H5q4imQqJyTaR1pmvBxCQ
"""

import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split

# Boston Housing Dataset
from  sklearn.datasets import load_boston
boston = load_boston()

# transform a data set into a data frame
# data  = the data we want or the independent variable aso known as the x values
# feature_names = the colmun names of the data
# target = the target variable or the price of the houses or dependent variable also known as the y value

df_x = pd.DataFrame(boston.data,columns=boston.feature_names)
df_y = pd.DataFrame(boston.target)

# Get some statistic from the data set such as set, count , mean
df_x.describe()

# Initialize the linear regressionn mode 
reg = linear_model.LinearRegression()

# Spliting the data ½80 traning ½20 testing
x_train , x_test , y_train , y_test = train_test_split(df_x ,df_y ,test_size = 0.20,random_state = 42)

# Train the model with our traning data
reg.fit(x_train,y_train)

# Print the coeffcients/ weight for each feature/colmuns of our model
print(reg.coef_) # f(x) = mx +b = y      --> m is the coef , ---> y dependent variable , ---> x independen variables

# Print the predictions on our test data 
y_pred = reg.predict(x_test)
# actual values  = y_test

# Check the model accuracy using Mean Squared Error
print(np.mean(
    (y_pred-y_test)**2
))

from sklearn.metrics import mean_squared_error
print(mean_squared_error(y_test,y_pred))

