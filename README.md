<img src='./imgs/AIAP-Banner.png'>

# Team 7 (FL Bricks) - aiap-team-7-project-jokebot
 This repo is used to document the mini-project for Team 7 (FL Bricks) where we deploy a pre-trained humour recognition model using a Streamlit app

 # Pipeline

 <img src='imgs/flowchart_v2.png'>

# Deployment
## Prerequisites
- miniconda or conda installed
- pre-trained model downloaded into models directory

### Setup conda environment
From project root directory:
```
conda env create -f project_requirements.yml
```
To update conda env with subsquent changes to .yml, run:
```
conda env update --name project-requirements --file project_requirements.yml --prune
```

### Download pre-trained model
download the model [here](https://mega.nz/folder/MmB1gIIT#8ilUTK1-BO80aoXxKOIhpg). unzip and place the folder "colbert-trained" under models(add "models" folder as well) in root directory of project, like so:
```
project-jokebot
        .
        .
        .
        |__scripts
        |__models
            |__colbert-trained
        |__src
        .
        .
        .
```

taken from: https://github.com/Moradnejad/ColBERT-Using-BERT-Sentence-Embedding-for-Humor-Detection
## Deployment stages
- Running locally
- Running local docker images
- Running on GKE

## Running locally
Our project runs the frontend on streamlit and backend on fastapi.

### prepare environment variables
From project's root directory:
```
export PRED_MODEL_PATH=$PWD/models/colbert-trained && \
export PRED_MODEL_UUID="colbert-trained"
```

### To run backend
From project's root directory:
```
cd src
gunicorn aiap_team_7_project_jokebot_fastapi.main:APP -b 0.0.0.0:8080 -w 2 -t 600 -k uvicorn.workers.UvicornWorker
```
to access FastAPI's docs, simply go to [here](http://localhost:8080/docs)(in your browser)
![](imgs/Screenshot-fastapi.png)

### To run frontend
From project's root directory:
```
streamlit run src/streamlit.py             
```
you should see a local web server opened in your browser like so:
![](imgs/Screenshot-streamlit.png)


## Running locally via Docker Images
before we deploy our applications on the cloud, we package scripts and modules as two seperate docker images. one to handle fronend user interface and another to another /predict requests coming from frontend

## Running on GKE
after building docker image, and pushed to cloud(GCP. We deploy these containers on GKE. This was only possible given that a GKE cluster was allocated during the course of our mini project. However, it is possible to modify, build, push and deploy these containers on a linux VM elsewhere.    

# Resources
- [cookie cutter template](https://github.com/aimakerspace/ml-project-cookiecutter-gcp/blob/master/README.md) -  template consisting of boilerplate codes and well-written docs with instructions on how to use.
- streamlit app: TODO
- gsutil bucket: gs://aiap-team-7-project-jokebot 
# Ground rules for project
- Initialised different branches for different features
    - main
    - dev
        - < feature >_< name working on feature>
    - production
- Choose a dataset and problem that is manageable: literature review
- Solidify all datasets -> split the work 
- rough outline of work required
    - Training,
        -  Data
        - Model (if SOTA already exists, transfer learn)
    - FastAPI
        - Preprocess endpoint
        - train endpoint 
        - infer endpoint
    - Final interation through UI (Usage/inference) 
        - streamlit need to call on your API
            - Going to have input form (file uploader or free form of your choice)
            - Send the data into the preprocess endpoint and forward into inference   

# References
- [Humor recognition using deep learning](https://aclanthology.org/N18-2018.pdf)
# Authors
Members
- Benjamin
- Chong Junn
- Guoren
- Jian Kai

Mentored by Mark
