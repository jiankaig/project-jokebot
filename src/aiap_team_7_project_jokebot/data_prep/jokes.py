import os
from google.cloud import storage
import json
import random


class Jokes:
    """
    Class to store the Jokes database

    Attributes
    ----------
    jokes: dict
        dictionary containing all the jokes from database (json file hosted on GCP available on: aiap-team-7-project-jokebot/data/shortjokes.json)
    jokes_count: int
        number of jokes present in the database (json file hosted on GCP available on: aiap-team-7-project-jokebot/data/shortjokes.json)

    Methods
    -------
    get_random_joke: str
        prints a random joke from the database
    """

    def __init__(
        self,
        bucketname: str = "aiap-team-7-project-jokebot",
        filename: str = "data/shortjokes.json",
        path_to_secret: str = "cred/gcp-service-account.json",
    ):
        self.jokes = self.__load_dataset_from_cloud(
            bucketname, filename, path_to_secret
        )
        self.jokes_count = len(self.jokes)

    def __load_dataset_from_cloud(
        self, bucketname: str, filename: str, path_to_secret_json: str
    ):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = path_to_secret_json
        storage_client = storage.Client()
        bucket = storage_client.get_bucket(bucketname)
        blob = bucket.blob(filename)
        dataset = json.loads(blob.download_as_string(client=None))
        return dataset

    def __random_joke_index(self):
        return str(random.randint(1, self.jokes_count - 1))

    def get_random_joke(self):
        return self.jokes[self.__random_joke_index()]
