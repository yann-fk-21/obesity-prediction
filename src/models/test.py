import pandas as pd

from sklearn.metrics import  accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import confusion_matrix

def accuracy_model(model, X: pd.DataFrame, y: pd.Series):
    return accuracy_score(y_true=y, y_pred=model.predict(X))

def recall_model(model, X: pd.DataFrame, y: pd.Series):
    return recall_score(y_true=y, y_pred=model.predict(X), average="weighted")

def precision_model(model, X: pd.DataFrame, y: pd.Series):
    return precision_score(y_true=y, y_pred=model.predict(X), average="weighted")

def confusion_matrix_model(model, X: pd.DataFrame, y: pd.Series):
    return confusion_matrix(y_true=y, y_pred=model.predict(X))



