import logging
import fastapi

import aiap_team_7_project_jokebot_fastapi as jokebot_fapi

logger = logging.getLogger(__name__)


ROUTER = fastapi.APIRouter()
# PRED_MODEL = jokebot_fapi.deps.PRED_MODEL_CUSTOM


@ROUTER.post("/predict", status_code=fastapi.status.HTTP_200_OK)
def predict_sentiment(joke_text: jokebot_fapi.schemas.InferJoke):
    """Endpoint that returns sentiment classification of movie review
    texts.

    Parameters
    ----------
    movie_reviews_json(deprecreted) : jokebot_fapi.schemas.MovieReviews
        'pydantic.BaseModel' object detailing the schema of the request
        body
    
    joke_text : jokebot_fapi.schemas.InferJoke of 'pydantic.BaseModel' class
            detailing the schema of the request body

    Returns
    -------
    dict
        Dictionary containing the sentiments for each movie review in
        the body of the request.

    Raises
    ------
    fastapi.HTTPException
        A 500 status error is returned if the prediction steps
        encounters any errors.
    """
    result_dict = {"data": []}
    result=""
    try:
        logger.info("Generating humour sentiments for .")
        
        # curr_pred_result = PRED_MODEL.predict(joke_text)
        curr_pred_result = 0.9
        sentiment = ("positive" if curr_pred_result > 0.5
                    else "negative")
        result = sentiment
        logger.info("Joke Sentiment generated for Humour ")

    except Exception as error:
        print(error)
        raise fastapi.HTTPException(
            status_code=500, detail="Internal server error.")

    return result


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
