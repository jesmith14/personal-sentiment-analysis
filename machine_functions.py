import pickle
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#helper function to make the input easier on the user but convert it to a useable array for the prediction values
def get_prediction_array_timeline(year, month, day, hour, minute):

    months = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if(month == 'April'):
        months[1] = 1
    elif(month == 'August'):
        months[2] = 1
    elif(month == 'December'):
        months[3] = 1
    elif(month == 'February'):
        months[4] = 1
    elif(month == 'July'):
        months[5] = 1
    elif(month == 'June'):
        months[6] = 1
    elif(month == 'March'):
        months[7] = 1
    elif(month == 'May'):
        months[8] = 1
    elif(month == 'November'):
        months[9] = 1
    elif(month == 'October'):
        months[10] = 1
    elif(month == 'September'):
        months[11] = 1
        
    return_year = [year]
    return_hour = [hour]
    return_minutes = [minute]
    return_day = [day]
    return_day_2 = [day ** 2]
    return_day_3 = [day ** 3]
    total_return = return_year + months + return_hour + return_minutes + return_day + return_day_2 + return_day_3
    return(total_return)
    
    
# Timeline
def getTimelinePrediction(year, month, day, hour, minute, timeline):
    months = pd.get_dummies(timeline["Month"]).drop("January", axis=1)
    dfs = [months, timeline[["Year", "Day", "Hour", "Minutes", "compound_score"]]]
    data_time = pd.concat(dfs, axis=1)
    data_time["Day^3"] = data_time["Day"] ** 3
    data_time["Day^2"] = data_time["Day"] ** 2
    prediction_values = get_prediction_array_timeline(year, month, day, hour, minute)
    X = data_time[["Year", 'April',
       'August', 'December', 'February', 'July', 'June', 'March', 'May',
       'November', 'October', 'September', 'Hour', 'Minutes', "Day", "Day^2", "Day^3"]]
    model = LinearRegression()
    model.fit(X, data_time["compound_score"])
    return(model.predict([prediction_values]))

#helper function to make the input easier on the user but convert it to a useable array for the prediction values
def get_prediction_array_messages(year, month, day, hour, minute):
    
    months = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if(month == 'April'):
        months[1] = 1
    elif(month == 'August'):
        months[2] = 1
    elif(month == 'December'):
        months[3] = 1
    elif(month == 'February'):
        months[4] = 1
    elif(month == 'July'):
        months[5] = 1
    elif(month == 'June'):
        months[6] = 1
    elif(month == 'March'):
        months[7] = 1
    elif(month == 'May'):
        months[8] = 1
    elif(month == 'November'):
        months[9] = 1
    elif(month == 'October'):
        months[10] = 1
    elif(month == 'September'):
        months[11] = 1
        
    return_year = [year]
    return_hour = [hour]
    return_minutes = [minute]
    return_day = [day]
    total_return = return_year + months + return_hour + return_minutes + return_day
    return(total_return)
    
# Messages
def getMessagePrediction(year, month, day, hour, minute, messages):
    months = pd.get_dummies(messages["Month"]).drop("January", axis=1)
    dfs = [months, messages[["Year", "Day", "Hour", "Minutes", "compound_score"]]]
    data_mess = pd.concat(dfs, axis=1)
    prediction_values = get_prediction_array_messages(year, month, day, hour, minute)
    X = data_mess[["Year", 'April',
       'August', 'December', 'February', 'July', 'June', 'March', 'May',
       'November', 'October', 'September', 'Day', 'Hour', 'Minutes']]
    model2 = LinearRegression()
    model2.fit(X, data_mess["compound_score"])
    return(model2.predict([prediction_values]))