import os
import logging
import hydra
import streamlit as st
import uvicorn
from PIL import Image

import aiap_team_7_project_jokebot as jokebot

GIF_FUNNY = "https://i.gifer.com/4j.gif"
GIF_UNFUNNY = "https://c.tenor.com/LI7vXH2DTuMAAAAC/the-office-michael-scott.gif"


@st.cache(allow_output_mutation=True)
def load_model(model_type, model_path):
    return jokebot.modeling.models.HumourRecognitionModel(model_type, model_path)


@hydra.main(config_path="../conf/base", config_name="pipelines.yml")
def main(args):
    """This main function does the following:
    - load logging config
    - loads trained model on cache
    - gets string input from user to be loaded for inferencing
    - conducts inferencing on string
    - outputs prediction results on the dashboard
    """

    logger = logging.getLogger(__name__)
    logger.info("Setting up logging configuration.")
    logger_config_path = os.path.join(
        hydra.utils.get_original_cwd(), "conf/base/logging.yml"
    )
    jokebot.general_utils.setup_logging(logger_config_path)

    model_type = args["inference"]["modeLtype"]
    model_path = os.path.join(
        hydra.utils.get_original_cwd(), args["inference"]["modelpath"]
    )
    imgs = os.path.join(hydra.utils.get_original_cwd(), args["inference"]["imgs"])

    logger.info("Loading the model...")
    pred_model = load_model(model_type, model_path)

    logger.info("Loading dashboard...")
    title = st.title("AIAP Team 7 Project Jokebot")

    text_input = st.text_area("Joke", placeholder="Insert your joke here")
    get_humour_sentiment = st.button("Get humour sentiment")

    waiting_text = st.empty()
    response = st.empty()
    gif_response = st.empty()

    if get_humour_sentiment:
        logger.info("Conducting inferencing on text input...")
        # TODO: curr_pred_result
        waiting_text.text("Waiting for the slow model to provide a response...")
        humour_level = pred_model.predict(text_input)
        waiting_text.text("")
        humour_percent = "{:.0%}".format(humour_level)
        logger.info(
            f"Inferencing has completed. Text input: {text_input}. Sentiment: {humour_percent}"
        )
        response.text(f"Your joke is {humour_percent} funny.")
        if humour_level > 0.5:
            markdown = f"![]({GIF_FUNNY})"

        else:
            markdown = f"![]({GIF_UNFUNNY})"

        gif_response.markdown(markdown)


if __name__ == "__main__":
    main()
