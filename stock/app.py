# app.py
from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

app = Flask(__name__)

# Load and preprocess the stock data from an Excel file
df = pd.read_csv('stock.csv')
df['date'] = pd.to_datetime(df['date'])

# Features and target
X = df[['open', 'high', 'low', 'volume']]
y = df['close']

# Train the model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    date = pd.to_datetime(data.get('date'))
    row = df[df['date'] == date]

    if row.empty:
        return jsonify({'error': 'No data available for the selected date'}), 400

    features = row[['open', 'high', 'low', 'volume']].values
    prediction = model.predict(features)
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
