# End-to-End_Data_Science:

The end-to-end DS for NBA dataset with deployement using PaaS Heroku:   

- Create a virtual env `python3 -m venv test_env`  
  Activate the env: `source test_env/bin/activate`  
  get all the packages: `pip install -r requirements.txt`

- To see the modeling part please follow Modeling.ipynb  

- To deploy the app on local server using Flask open app.py file.  
  You can run the app.py file in terminal `python app.py`  

- To view the deployed app on Heroku PaaS follow the link: https://player-stats-nba.herokuapp.com/

### Files

- nba_logreg.csv: the csv file for training and validating

- Modeling.ipynb: The jupyter file which performs the EDA/processing and rolls out the final ML model

- app.py: The file which uses Flask to locally serve the model 

- model.pkl: the final model

- scaler.pkl: the pkl file for normalising the input, before performing the predict

- Procfile: For deploying the app on PaaS Heroku

- requirements.txt: For creating a virtual env 
