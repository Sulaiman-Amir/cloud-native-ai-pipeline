import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Load dataset (dummy example)
data = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
X = data.drop('species', axis=1)
y = data['species']

# Train model
clf = RandomForestClassifier()
clf.fit(X, y)

# Save model to file
joblib.dump(clf, os.path.join('/opt/ml/model', 'model.joblib'))

