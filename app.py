from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open('model/wine_quality_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Home route to render the HTML form
@app.route('/')
def home():
    return render_template('index.html')  # Ensure your HTML file is named 'index.html' and located in the 'templates' folder


# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = [
        data['fixed_acidity'],
        data['volatile_acidity'],
        data['citric_acid'],
        data['residual_sugar'],
        data['chlorides'],
        data['free_sulfur_dioxide'],
        data['total_sulfur_dioxide'],
        data['density'],
        data['pH'],
        data['sulphates'],
        data['alcohol']
    ]
    prediction = model.predict([features])[0]
    return jsonify({'quality': int(prediction)})

if __name__ == '__main__':
    app.run(debug=True)
