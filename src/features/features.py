import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler,LabelEncoder
from sklearn.model_selection import train_test_split

def transform_label(data: pd.Series):
    label = LabelEncoder()
    return label.fit_transform(y=data)

def preprocessing_data(data: pd.DataFrame, target: str):
    y = data[target]
    X = data.drop(columns=target, axis=1)

    X_train, X_test_val, y_train, y_test_val = train_test_split(X, y, test_size=0.2,
                                                        random_state=42)
    X_test, X_val, y_test, y_val = train_test_split(X_test_val, y_test_val, test_size=0.5,
                                                    random_state=42)

    prepare_pipeline = Pipeline(steps=[
        ("impute", SimpleImputer(strategy="mean")),
        ("scaler", MinMaxScaler())
    ])

    X_train_tr = prepare_pipeline.fit_transform(X_train)
    X_val_tr = prepare_pipeline.transform(X_val)
    X_test_tr = prepare_pipeline.transform(X_test)


    return (X_train_tr, y_train), (X_val_tr, y_val), (X_test_tr, y_test)

