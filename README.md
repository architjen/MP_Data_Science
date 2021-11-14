# This repo contains end-to-end Data Science project:

## Project
The NBA officials would like to know if a certain player should be signed or not based on his stats. They provide you with the [dataset](nba_logreg.csv) to further build a ML classifier. Here, we perform the end-to-end DS task, which are:   

**EDA** --> Data Analysis, and processing  
**ML modeling** --> Performing benchmark testing on all vanilla models, fine tuning the most outperforming   
**Model deployment** --> Local: using Flask for local deployment **|** Live: using Heroku (Paas) for live deployment 

## Files

```
MP_Data_Science  
  |  
  |---static   
  |     |  
  |     |---css 
  |          |
  |          |---style.css: styling the deployment page
  |
  |---templates    
  |     |
  |     |---index.html: used as a request form on deplyment page to get the value from users
  |
  |---.gitignore: Describes the files and folders which shouldnt be pushed in the repo
  |
  |---Modeling.ipynb: The jupyter notebook that performs the EDA and modeling
  |
  |---Procfile: to serve the live deployment on Heroku
  |
  |---README.md: You are looking at me
  |
  |---app.py: Flask API endpoint script
  |
  |---model.pkl: The ML model served on the API for getting the predictions
  |
  |---nba_logreg.csv: The csv data used for the project 
  |
  |---requirements.txt: List of all necessary packages for the building an env
  |
  |---scaler.pkl: The file to normalise the input data (retrieved from the API)
  |
  |---test.py: The file for performing testing (TO DO)
```

## Building the env and testing   
The task is performed using Python 3.9.7

### Build
- Clone the repo locally
- Create a virtual env `python3 -m venv test_env`  
  Activate the env: `source test_env/bin/activate`  
  get all the packages: `pip install -r requirements.txt`

### Testing
- To see the modeling part please follow Modeling.ipynb  

- To deploy the app on local server using Flask open app.py file.  
  You can run the app.py file in terminal `python app.py`  

- To view the deployed app on Heroku PaaS follow the link: https://player-stats-nba.herokuapp.com/

