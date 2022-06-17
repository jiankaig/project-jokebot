# Project Jokebot
Project jokebot is a simple web-based application (using streamlit app) where it allows aspiring comedians to understand the 'joke rating' of their jokes.


## Table of content

- [Pipeline](#pipeline)
- [Deployment](#deployment)
    - [Prerequisites](#prerequisites)
    - [Running locally](#running-locally)
    - [To run frontend](#to-run-frontend)
    - [To run backend](#to-run-backend)
    - [Running locally via Docker Images](#running-locally-via-docker-images)
    - [Running on GKE](#running-on-gke)
- [References](#references)
- [Contributors](#contributors)

## Demonstration

![](https://j.gifs.com/mqVvKA.gif)

 ## Pipeline
 <img src='imgs/flowchart_v2.png'>

## Deployment
### Prerequisites
- conda env
- models folder
- 
### Deployment stages
- Running locally
- Running local docker images
- Running on GKE

### Running locally
Our project runs the frontend on streamlit and backend on fastapi.


#### To run frontend
```
streamlit run src/streamlit.py             
```

#### To run backend
```
cd src
gunicorn aiap_team_7_project_jokebot_fastapi.main:APP -b 0.0.0.0:8080 -w 2 -t 600 -k uvicorn.workers.UvicornWorker
```
### Running locally via Docker Images

### Running on GKE



## References
- [Humor recognition using deep learning](https://aclanthology.org/N18-2018.pdf)
- [colBERT using BERT Sentence Embedding for humour detection](https://github.com/Moradnejad/ColBERT-Using-BERT-Sentence-Embedding-for-Humor-Detection) 
## Contributors
- Benjamin
- [Chong Junn](https://github.com/chongjunn-tech)
- [Guoren](https://github.com/nguoren)
- [Jian Kai](https://github.com/jiankaig)


