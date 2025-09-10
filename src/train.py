from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib
from src.preprocessing import load_and_split_data

X_train, X_test, y_train, y_test = load_and_split_data('data/train.csv')

model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

preds = model.predict(X_test)
print("MSE:", mean_squared_error(y_test, preds))

joblib.dump(model, 'models/model.pkl')
