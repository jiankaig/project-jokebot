<img src='./imgs/AIAP-Banner.png'>

# Team 7 (FL Bricks) - aiap-team-7-project-jokebot
 This repo is used to document the mini-project for Team 7 (FL Bricks) where we deploy a pre-trained humour recognition model using a Streamlit app

 # Pipeline

 <img src='./imgs/flowchart.png'>

# Resources
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
