from sklearn.ensemble import RandomForestClassifier
import pickle
import numpy as np

# Simulated data
X = np.random.rand(100, 3) * 100
y = (X[:, 0] + X[:, 1] + X[:, 2] > 150).astype(int)  # 1 = unhealthy

model = RandomForestClassifier()
model.fit(X, y)

with open("predictor/health_model.pkl", "wb") as f:
    pickle.dump(model, f)
