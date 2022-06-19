import os
import logging
import streamlit as st
import requests

import aiap_team_7_project_jokebot as jokebot

FASTAPI_SERVER_IP = "localhost"
# FASTAPI_SERVER_IP = "fastapi-server-team-7-svc"

GIF_FUNNY = "https://i.gifer.com/4j.gif"
GIF_UNFUNNY = "https://c.tenor.com/LI7vXH2DTuMAAAAC/the-office-michael-scott.gif"
logger = logging.getLogger(__name__)


@st.cache(allow_output_mutation=True)
def load_model(model_type, model_path):
    return jokebot.modeling.models.HumourRecognitionModel(model_type, model_path)


def rate_joke():
    text_input = st.text_area("Joke", placeholder="Insert your joke here")
    get_humour_sentiment = st.button("Get humour sentiment")

    waiting_text = st.empty()
    response = st.empty()
    gif_response = st.empty()

    if get_humour_sentiment:
        logger.info("Conducting inferencing on text input...")
        waiting_text.text("Waiting for the slow model to provide a response...")
        ret = requests.post(
            f"http://{FASTAPI_SERVER_IP}:8080/api/v1/model/predict",
            json={"joke": text_input},
        ).json()
        humour_level = float(ret["data"].get("score"))
        waiting_text.text("")
        humour_percent = "{:.0%}".format(humour_level)
        logger.info(
            f"Inferencing has completed. Text input: {text_input}. Sentiment: {humour_percent}"
        )
        response.text(f"Your joke is {humour_percent} funny.")
        if humour_level >= 0.5:
            markdown = f"![]({GIF_FUNNY})"

        else:
            markdown = f"![]({GIF_UNFUNNY})"

        gif_response.markdown(markdown)


def generate_joke():
    text_input = st.text_area("Generate joke", placeholder="Insert start of joke here")
    generate_joke_button = st.button("Get the joke for me!")
    waiting_text = st.empty()
    response = st.empty()
    if generate_joke_button:
        waiting_text.text("Waiting for response")
        ret = requests.post(
            f"http://{FASTAPI_SERVER_IP}:8080/api/v1/model/generate-joke",
            json={"text": text_input},
        ).json()
        waiting_text.text(f"Joke generated..")
        response.markdown(f"{ret['data'].get('generated_joke')}")


FACTORIES = {
    "Rate joke": rate_joke,
    "Generate joke": generate_joke,
}


def read_factory(selected):
    if FACTORIES.get(selected):
        return FACTORIES.get(selected)()
    else:
        raise Exception("Not implemented")


def main():
    """This main function does the following:
    - load logging config
    - loads trained model on cache
    - gets string input from user to be loaded for inferencing
    - conducts inferencing on string
    - outputs prediction results on the dashboard
    """

    logger.info("Loading dashboard...")
    title = st.markdown("# :laughing: Project Jokebot :laughing: ")

    with st.sidebar:
        selected = st.radio("Navigation", (FACTORIES.keys()))
    read_factory(selected)


if __name__ == "__main__":
    main()
