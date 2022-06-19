import aiap_team_7_project_jokebot as jokebot
import aiap_team_7_project_jokebot_fastapi as jokebot_fapi
from aiap_team_7_project_jokebot.modeling import models

PRED_MODEL = jokebot.modeling.utils.load_model(
    jokebot_fapi.config.SETTINGS.PRED_MODEL_PATH
)

PRED_MODEL_CUSTOM = jokebot.modeling.models.HumourRecognitionModel(
    path_to_saved_model=jokebot_fapi.config.SETTINGS.PRED_MODEL_PATH
)

JOKE_GENERATOR = jokebot.modeling.models.JokeGenerator(
    jokebot_fapi.config.SETTINGS.JOKE_GENERATOR_MODEL,
    jokebot_fapi.config.SETTINGS.MAX_LENGTH,
)
