from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

import pandas as pd

def train_svm_model(X: pd.DataFrame, y: pd.Series):
    model = SVC()
    model.fit(X, y)
    return model

def train_random_forest_model(X: pd.DataFrame, y: pd.Series):
    model = RandomForestClassifier()
    model.fit(X, y)
    return model

def train_logistic_reg_model(X: pd.DataFrame, y: pd.Series):
    model = LogisticRegression()
    model.fit(X, y)
    return model

def train_knn_model(X: pd.DataFrame, y: pd.Series):
    model = KNeighborsClassifier()
    model.fit(X, y)
    return model

def fine_tuning_model(model, X, y, grid_params, cv):
    model = GridSearchCV(estimator=model, param_grid=grid_params, cv=cv, scoring="accuracy")
    model.fit(X, y)
    return model