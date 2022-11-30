from flask import Flask, request
import os
import joblib

joblib_model = joblib.load("/home/model-server/joblib_model.pkl")

app = Flask(__name__)
  
@app.route('/predict', methods=["GET", "POST"])
def predict():
    if request.method=="POST":
        inputs = request.json['inputs']
        # model.predict(n=26, inputs)
        
        return {"status": "Received Data", "prediction": 20}
    else:
        return "Hello World"
  
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5050)))