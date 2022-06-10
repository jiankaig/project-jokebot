import os
import logging
import hydra
import streamlit as st
import uvicorn

import aiap_team_7_project_jokebot as jokebot

@st.cache(allow_output_mutation=True)
def load_model(model_path):
    return jokebot.modeling.utils.load_model(model_path)

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
    logger_config_path = os.path.\
        join(hydra.utils.get_original_cwd(),
            "conf/base/logging.yml")
    jokebot.general_utils.setup_logging(logger_config_path)

    logger.info("Loading the model...")
    pred_model = load_model(args["inference"]["model_path"])

    logger.info("Loading dashboard...")
    title = st.title('AIAP Team 7 Project Jokebot')

    text_input = st.text_area("Review",
        placeholder="Insert your review here")

    if st.button("Get sentiment"):
        logger.info("Conducting inferencing on text input...")
        # TODO: curr_pred_result
        curr_pred_result = float(pred_model.predict([text_input])[0])
        sentiment = ("positive" if curr_pred_result > 0.5
                    else "negative")
        logger.info(
            "Inferencing has completed. Text input: {}. Sentiment: {}"
            .format(text_input, sentiment))
        st.write("The sentiment of the review is {}."
            .format(sentiment))
    else:
        st.write("Awaiting a review...")

if __name__ == "__main__":
    main()