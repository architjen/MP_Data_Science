#The Flask webservice file 

import numpy as np
from flask import Flask, request, render_template
import pickle

# create Flask app
app = Flask(__name__)

#load model
model = pickle.load(open('model.pkl', 'rb'))

#scaler for normalising the features
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    scaled_final_features = scaler.transform(final_features)
    prediction = model.predict(scaled_final_features)

    return render_template('index.html', prediction_text='The player would be $ {}'.format(prediction))

if __name__ == "__main__":
    app.run(debug=True)