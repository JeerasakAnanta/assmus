from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the trained machine learning model
model = joblib.load("sentiment_analysis_model.joblib")

@app.route("/predict", methods=["POST"])
def predict():
    # Get the text data from the request
    data = request.json
    text = data["text"]

    # Make predictions using the model
    prediction = model.predict([text])[0]

    # Return the predicted sentiment
    return jsonify({"sentiment": prediction})

if __name__ == "__main__":
    app.run(debug=True)
