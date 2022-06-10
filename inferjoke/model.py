from helper.inferJoke_helper import *
import keras
import pandas as pd
import logging
from transformers import BertTokenizer


class HumourRecognitionModel:
    def __init__(
        self,
        model_type: str = "bert-base-uncased",
        path_to_saved_model: str = "../aiap-team-7-project-jokebot/models/colbert-trained/",
    ) -> None:
        self.tokenizer = BertTokenizer.from_pretrained(model_type)
        self.model = keras.models.load_model(path_to_saved_model)

    def predict(self, joke):
        return evalJoke(self.model, joke, self.tokenizer)


def evalJoke(model, joke, tokenizer, columns=["text"]):
    X = pd.DataFrame([joke], columns=["text"])
    X = compute_input_arrays(X, columns=columns, tokenizer=tokenizer)
    ypred = model.predict(X)
    return evalPred(ypred, threhold=0.5)


def main():
    X = "I invented a new word!\nPlagiarism!"

    logger = logging.getLogger(__name__)
    logger.info("try infer from saved model experiment")

    model = HumourRecognitionModel()
    model.predict(X)


if __name__ == "__main__":
    main()
