import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

from sklearn.ensemble import RandomForestClassifier  # For classification tasks

from sklearn.metrics import accuracy_score  # For classification tasks

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from xgboost import XGBRegressor
from sklearn.multioutput import MultiOutputRegressor
from sklearn.ensemble import BaggingRegressor

import xgboost as xgb
import numpy as np
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report

data = pd.read_csv('./clustered_data_200/combined_file_200.csv')



# Separate features and target
# X = data[['delay', 'area', 'power', 'Median']]
# y = data['target'].apply(lambda x: str(x))  # Convert target to string

y = data["Multiplier"]
X = data.drop(["Multiplier"],axis=1)
X['SSIM'] = X['SSIM'] * 10000

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

import cudf

df_x_train = pd.DataFrame(X_train)
df_x_test = pd.DataFrame(X_test)

X_train_cudf = cudf.from_pandas(df_x_train)
X_test_cudf = cudf.from_pandas(df_x_test)
y_train_cudf = cudf.Series(y_train-1)
y_test_cudf = cudf.Series(y_test)

print(X_train_cudf.shape)

import cupy as cp

X_train_cupy = cp.array(X_train)
y_train_cupy = cp.array(y_train-1)
X_test_cupy = cp.array(X_test)
y_test_cupy = cp.array(y_test)

print(X_train_cupy.shape)

# Define the parameter grid
# param_grid = {
#     'max_depth': [3, 4, 5, 6],
#     'learning_rate': [0.01, 0.1, 0.2],
#     'n_estimators': [100, 200, 300],
#     'min_child_weight': [1, 3, 5],
#     'subsample': [0.8, 0.9, 1.0],
#     'colsample_bytree': [0.8, 0.9, 1.0]
# }
param_grid = {
    'max_depth': [3, 6],
    'learning_rate': [ 0.1, 0.2],
    'n_estimators': [100, 200],
    'min_child_weight': [ 3, 5],
    'subsample': [0.8, 0.9, 1.0],
    'colsample_bytree': [0.8, 0.9, 1.0]
}
# Create the XGBoost classifier
xgb = XGBClassifier(eval_metric='mlogloss', random_state=42, device ='cuda', max_bin=64,  predictor = 'gpu_predictor', n_thread = 2, n_gpus=1)
print("xgb done")
# Perform GridSearchCV
# grid_search = GridSearchCV(estimator=xgb, param_grid=param_grid, cv=5, n_jobs=-1, verbose=2)
grid_search = GridSearchCV(estimator=xgb, param_grid=param_grid, cv=5,verbose=1, n_jobs=1)
# print("grid search done")

# # grid_search.fit(X_train, y_train-1)
grid_search.fit(X_train, y_train-1)

# xgb.fit(X_train_cupy, y_train_cupy)



# Get the best parameters
best_params = grid_search.best_params_
print("Best parameters:", best_params)