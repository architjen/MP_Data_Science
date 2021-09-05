import numpy as np
import pickle

#load model
model = pickle.load(open('model.pkl', 'rb'))

#scaler for normalising the features
scaler = pickle.load(open('scaler.pkl', 'rb'))


float_features = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
final_features = [np.array(float_features)]
scaled_features = scaler.transform(final_features)
prediction = model.predict(scaled_features)
