import os
import logging
import hydra
import streamlit as st

import aiap_team_7_project_jokebot as jokebot


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

    logger.info("Loading the model...")
    pred_model = load_model(model_type, model_path)

    logger.info("Loading dashboard...")
    title = st.title("AIAP Team 7 Project Jokebot")

    text_input = st.text_area("Review", placeholder="Insert your jokes here")

    if st.button("Get humour sentiment"):
        logger.info("Conducting inferencing on text input...")
        # TODO: curr_pred_result

        sentiment = pred_model.predict(text_input)
        # curr_pred_result = float(pred_model.predict([text_input])[0])
        # sentiment = "positive" if curr_pred_result > 0.5 else "negative"
        logger.info(
            f"Inferencing has completed. Text input: {text_input}. Sentiment: {sentiment}"
        )
        st.write(f"The sentiment of the joke is {sentiment}.")
    else:
        st.write("Awaiting a review...")


if __name__ == "__main__":
    main()
