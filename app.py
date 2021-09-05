#The Flask webservice file 
#To run the file `python app.py`

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
    #get the list of features
    float_features = [float(x) for x in request.form.values()]
    
    #converts them to 2d array
    final_features = [np.array(float_features)]
    
    #apply the normalisation on the features
    scaled_final_features = scaler.transform(final_features)
    
    #predict the features
    prediction = model.predict(scaled_final_features)

    #returning the statement instead of 0 and 1
    if prediction == 1:
        ans = 'would last 5 years in NBA'
    else:
        ans = 'wouldnt last 5 years in NBA'


    return render_template('index.html', prediction_text='The player {}'.format(ans))

if __name__ == "__main__":
    app.run(debug=True)