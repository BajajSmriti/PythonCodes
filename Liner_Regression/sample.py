# -*- coding: utf-8 -*-
from math import sqrt

def mean(values):
    return sum(values)/(len(values))

def covariance(x,mean_x,y,mean_y):
    covar=0.0
    for i in range(len(x)):
        covar+=(x[i]-mean_x)*(y[i]-mean_y)
    return covar

def variance(values,mean):
    return sum([(x-mean)**2 for x in values])

def coefficients(dataset):
    x = [row[0] for row in dataset]
    y = [row[1] for row in dataset] 
    x_mean, y_mean = mean(x), mean(y)
    x1 = covariance(x, x_mean, y, y_mean) / variance(x, x_mean)
    x0 = y_mean - x1 * x_mean 
    return [x0,x1]

def rmse_prediction(actual, predicted):
    sum_error = 0.0
    for i in range(len(actual)):
        prediction_error = predicted[i] - actual[i]
        sum_error += (prediction_error **2)
    mean_error = sum_error / (len(actual))
    return sqrt(mean_error)

def simple_linear_regression(train, test):
    predictions = list()
    b0, b1 = coefficients(train)
    for row in test :
        yhat= b0 + b1 * row[0]
        predictions.append (yhat)
    return predictions

def manage_prediction(dataset, algorithm):
    test_set = list()
    for row in dataset:
        row_copy = list(row)
        row_copy[-1] = None
        test_set.append(row_copy)
    predicted = algorithm(dataset, test_set)
    actual = [row[-1] for row in dataset]
    rootmeansquaredError = rmse_prediction(actual, predicted)
    return rootmeansquaredError

dataset=[1,10],[2,20],[3,30],[4,20],[5,50],[6,60]
rootmeansquaredError=manage_prediction(dataset,simple_linear_regression)
print('Root mean squared Error:%3f' %(rootmeansquaredError))