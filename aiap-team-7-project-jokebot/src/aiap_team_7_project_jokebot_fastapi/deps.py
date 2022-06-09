import aiap_team_7_project_jokebot as jokebot
import aiap_team_7_project_jokebot_fastapi as jokebot_fapi


PRED_MODEL = jokebot.modeling.utils.load_model(
    jokebot_fapi.config.SETTINGS.PRED_MODEL_PATH)
