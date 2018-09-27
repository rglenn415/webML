import sklearn
import numpy as np
from sklearn.model_selection import train_test_split
#used to perform logistic regression
from sklearn.linear_model import LogisticRegression
#used for logistic regression metrics
from sklearn.metrics import classification_report
from sklearn import model_selection
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import cross_val_score
import sys
import pandas as pd
import pickle as pkl
from bson.binary import Binary #part of pymongo
import pymongo

def create_model(userData):
    #save csv file with headers still on it for later use
    csv = userData

    #pop the column headers
    headers = userData['file'].pop(0)

    selectedFeature = userData['selectedFeature']
    df = pd.DataFrame(userData['file'],columns=headers)

    #preprocessing
    target = df[selectedFeature]

    #drops the selected COLUMN feature from user input
    features = df.drop(selectedFeature, axis =1)

    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=.2, random_state=7)

    #create and train model
    model = LogisticRegression()
    model.fit(X_train,y_train)


    accuracy_results = cross_val_score(model, features, target, scoring='accuracy')
    acc = accuracy_results.mean()
    #print(f'Accuracy: {round(acc*100,1)}%')
    y_pred = cross_val_predict(model,features,target)
    c_matrix = confusion_matrix(target,y_pred)
    #print(f'Confusion Matrix:\n {c_matrix}')
    c_report = classification_report(target,y_pred)
    #print(f'Classificaiton Report:\n{c_report}')


    encoded_list = encode([model,csv,acc,c_matrix.tolist(),c_report])

    #open mongodb connection
    myclient = pymongo.MongoClient('mongodb://localhost:27017/')
    #refrence the webML database
    mydb = myclient['webML']
    #refrence the runs collection inside webML
    mycol =  mydb['runs']


    #define the data
    encoded_data = {'model':encoded_list[0],'csv':encoded_list[1],'accuracy':encoded_list[2],'confusion':encoded_list[3],'classifcation':encoded_list[4]}
    reporting_data = {'accuracy':acc,'confusion':c_matrix.tolist(),'classification':c_report}



    #insert the data into the runs collection
    mycol.insert_one(encoded_data)

    return reporting_data

def encode(unencoded_list):
    encoded_list = []
    for item in unencoded_list:
        #first dumps pickle and then encodes in binary
        item_pkl = Binary(pkl.dumps(item))
        encoded_list.append(item_pkl)
    return encoded_list




