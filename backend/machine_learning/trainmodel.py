# Example: Train a scikit-learn model and save it to disk
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load your training data and preprocess it
# ...

# Train your model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the trained model to disk
joblib.dump(model, 'ml_models/my_model.pkl')
