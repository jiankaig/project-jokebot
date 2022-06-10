import aiap_team_7_project_jokebot as jokebot
import aiap_team_7_project_jokebot_fastapi as jokebot_fapi
from aiap_team_7_project_jokebot.modeling import models

# from .. import aiap_team_7_project_jokebot as jokebot
# from .. import aiap_team_7_project_jokebot_fastapi as jokebot_fapi

PRED_MODEL = jokebot.modeling.utils.load_model(
    jokebot_fapi.config.SETTINGS.PRED_MODEL_PATH)

PRED_MODEL_CUSTOM = jokebot.modeling.models.HumourRecognitionModel(path_to_saved_model=jokebot_fapi.config.SETTINGS.PRED_MODEL_PATH)