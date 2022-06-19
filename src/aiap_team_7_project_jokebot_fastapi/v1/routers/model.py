import logging
import fastapi

import aiap_team_7_project_jokebot_fastapi as jokebot_fapi

logger = logging.getLogger(__name__)


ROUTER = fastapi.APIRouter()

MODELS = {}


@ROUTER.on_event("startup")
async def startup_event():
    PRED_MODEL = jokebot_fapi.deps.PRED_MODEL_CUSTOM
    JOKE_GENERATOR = jokebot_fapi.deps.JOKE_GENERATOR
    MODELS["PRED_MODEL"] = PRED_MODEL
    MODELS["JOKE_GENERATOR"] = JOKE_GENERATOR


@ROUTER.post("/predict", status_code=fastapi.status.HTTP_200_OK)
def predict_sentiment(joke_text: jokebot_fapi.schemas.InferJoke):
    """Endpoint that returns humour sentiment (float) of joke provided by user

    Parameters
    ----------
    joke_text : jokebot_fapi.schemas.InferJoke of 'pydantic.BaseModel' class
            detailing the schema of the request body

    Returns
    -------
    dict
        Dictionary containing the humour sentiment (score) for joke in
        the body of the request.

    Raises
    ------
    fastapi.HTTPException
        A 500 status error is returned if the prediction steps
        encounters any errors.
    """
    try:
        logger.info(f"Generating humour sentiments for {joke_text.joke}")
        logger.info(f"[DEBUG] joke: {joke_text.joke}")
        score = MODELS["PRED_MODEL"].predict(joke_text.joke)
        logger.info("Joke Sentiment generated for Humour ")

    except Exception as error:
        print(error)
        raise fastapi.HTTPException(status_code=500, detail="Internal server error.")

    return {"data": {"score": str(score)}}


@ROUTER.post("/generate-joke", status_code=fastapi.status.HTTP_200_OK)
def generate_joke(pregen_text: jokebot_fapi.schemas.PreGenText):
    """Endpoint that generate a 'joke' based on text provided by user

    joke_text : jokebot_fapi.schemas.PreGenText of 'pydantic.BaseModel' class
            detailing the schema of the request body

    Returns
    -------
    dict
        Dictionary containing the generated joke (str) in
        the body of the request.

    Raises
    ------
    fastapi.HTTPException
        A 500 status error is returned if the prediction steps
        encounters any errors.
    """
    try:
        logger.info(f"Generating joke for {pregen_text.text}.")

        generated_joke = MODELS["JOKE_GENERATOR"].generate_joke(pregen_text.text)
        logger.info("Joke generated...")

    except Exception as error:
        print(error)
        raise fastapi.HTTPException(status_code=500, detail="Internal server error.")

    return {"data": {"generated_joke": generated_joke}}


@ROUTER.get("/version", status_code=fastapi.status.HTTP_200_OK)
def get_model_version():
    """Get version (UUID) of predictive model used for the API.

    Returns
    -------
    dict
        Dictionary containing the UUID of the predictive model being
        served.
    """
    return {"data": {"model_uuid": jokebot_fapi.config.SETTINGS.PRED_MODEL_UUID}}
