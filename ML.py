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

def create_model(userData):
    #save csv file with headers still on it for later use
    csv = userData['file']

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
    print(f'Accuracy: {round(acc*100,1)}%')
    y_pred = cross_val_predict(model,features,target)
    c_matrix = confusion_matrix(target,y_pred)
    print(f'Confusion Matrix:\n {c_matrix}')
    c_report = classification_report(target,y_pred,target_names=headers)
    print(f'Classificaiton Report:\n{c_report}')

    #encode csv and model with pickle

    data = {'model':,'csv':,'accuracy':acc,'confusion':c_matrix,'classifcation',c_report}




    #reporting
        #test with train data
            #confusion matrix
            #accuracy report

