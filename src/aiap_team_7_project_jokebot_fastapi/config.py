import pydantic


class Settings(pydantic.BaseSettings):

    API_NAME: str = "aiap_team_7_project_jokebot_fastapi"
    API_V1_STR: str = "/api/v1"
    LOGGER_CONFIG_PATH: str = "../conf/base/logging.yml"

    PRED_MODEL_UUID: str
    PRED_MODEL_PATH: str

    # joke generator settings
    JOKE_GENERATOR_MODEL: str = "huggingtweets/dadsaysjokes"
    MAX_LENGTH: int = 100


SETTINGS = Settings()
