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
import sys

def model(userData):
    #print(userData['file'], file=sys.stdout)
    
    train, test = train_test_split(userData['file'], test_size=.2)
    print(len(train),len(test), file=sys.stdout)
    #split
        #extract target feature from userdata
        #extract csv from userdata
        #train test split userdata
        #remove feature from train and test into lists
    #train
        #create model
        #train model with train data
    #reporting
        #test with train data
            #confusion matrix
            #accuracy report
