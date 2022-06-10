from helper.inferJoke_helper import *
import keras
import pandas as pd
import logging
from transformers import BertTokenizer

def evalJoke(model, joke, tokenizer, columns=['text']):
    X = pd.DataFrame([joke], columns=['text'])
    X = compute_input_arrays(X, columns=columns, tokenizer=tokenizer)
    ypred = model.predict(X)
    return evalPred(ypred,threhold=0.5)

def main():
    # X = "Black teen's response to violence in his"
    X = "I invented a new word!\nPlagiarism!"

    logger = logging.getLogger(__name__)
    logger.info("try infer from saved model experiment")


    MODEL_TYPE = 'bert-base-uncased'
    tokenizer = BertTokenizer.from_pretrained(MODEL_TYPE)
    
    model = keras.models.load_model("../aiap-team-7-project-jokebot/models/colbert-trained/")
    return evalJoke(model, X, tokenizer)

if __name__ == "__main__":
    main()