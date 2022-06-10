#!/bin/bash

set -x

source ~/.bashrc >/dev/null

streamlit run src/streamlit.py -- inference.model_path=$PRED_MODEL_PATH
