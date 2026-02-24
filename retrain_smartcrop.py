import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB

# Read Data
df = pd.read_csv('SmartCrop-Dataset.csv')

# Remove Outliers on numeric columns only
numeric_df = df.drop('label', axis=1)
Q1 = numeric_df.quantile(0.25)
Q3 = numeric_df.quantile(0.75)
IQR = Q3 - Q1
df_out = df[~((numeric_df < (Q1 - 1.5 * IQR)) |(numeric_df > (Q3 + 1.5 * IQR))).any(axis=1)]

# Split Data
X = df_out.drop('label', axis=1)
y = df_out['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train model
pipeline = make_pipeline(StandardScaler(), GaussianNB())
model = pipeline.fit(X_train, y_train)

# Save Trained Model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("SmartCrop model retrained and saved successfully at model.pkl!")
