from flask import Flask, request, jsonify
import joblib
import pandas as pd
import os

app = Flask(__name__)


model = joblib.load('best_svm_model.pkl')
preprocessor = joblib.load('preprocessor.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    df = pd.DataFrame(data, index=[0])
    df_processed = preprocessor.transform(df)
    prediction = model.predict(df_processed)
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
