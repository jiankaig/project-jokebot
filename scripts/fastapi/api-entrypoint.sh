#!/bin/bash

set -x

source ~/.bashrc

python -m nltk.downloader punkt

gcloud auth activate-service-account --key-file $GOOGLE_APPLICATION_CREDENTIALS

if [ ! -d "$PRED_MODEL_PATH" ]; then
    gsutil cp -r $PRED_MODEL_GCS_URI $HOME/from-gcs
fi

cd src
gunicorn aiap_team_7_project_jokebot_fastapi.main:APP -b 0.0.0.0:8080 -w 4 -k uvicorn.workers.UvicornWorker -t 6000