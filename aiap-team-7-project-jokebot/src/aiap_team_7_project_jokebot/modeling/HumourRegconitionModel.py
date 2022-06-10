import keras
import pandas as pd
import numpy as np
import sklearn
from transformers import BertTokenizer
from tqdm.notebook import tqdm
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
import logging


class HumourRecognitionModel:
    def __init__(
        self,
        model_type: str = "bert-base-uncased",
        path_to_saved_model: str = "../aiap-team-7-project-jokebot/models/colbert-trained/",
    ) -> None:
        self.tokenizer = BertTokenizer.from_pretrained(model_type)
        self.model = keras.models.load_model(path_to_saved_model)
        
        self.MAX_SENTENCE_LENGTH = 20
        self.MAX_SENTENCES = 5
        self.MAX_LENGTH = 100

    def predict(self, joke):
        return self._evalJoke(self.model, joke, self.tokenizer)
    

    def _return_id(str1, str2, truncation_strategy, length,tokenizer):

        inputs = tokenizer.encode_plus(str1, str2,
            add_special_tokens=True,
            max_length=length,
            truncation_strategy=truncation_strategy)

        input_ids =  inputs["input_ids"]
        input_masks = [1] * len(input_ids)
        input_segments = inputs["token_type_ids"]
        padding_length = length - len(input_ids)
        padding_id = tokenizer.pad_token_id
        input_ids = input_ids + ([padding_id] * padding_length)
        input_masks = input_masks + ([0] * padding_length)
        input_segments = input_segments + ([0] * padding_length)

        return [input_ids, input_masks, input_segments]


    def _compute_input_arrays(df, columns, tokenizer):
        model_input = []
        for xx in range((self.MAX_SENTENCES*3)+3):
            model_input.append([])
        
        for _, row in tqdm(df[columns].iterrows()):
            i = 0
            
            # sent
            sentences = sent_tokenize(row.text)
            for xx in range(self.MAX_SENTENCES):
                s = sentences[xx] if xx<len(sentences) else ''
                ids_q, masks_q, segments_q = self._return_id(s, None, 'longest_first', self.MAX_SENTENCE_LENGTH,tokenizer)
                model_input[i].append(ids_q)
                i+=1
                model_input[i].append(masks_q)
                i+=1
                model_input[i].append(segments_q)
                i+=1
            
            # full row
            ids_q, masks_q, segments_q = return_id(row.text, None, 'longest_first', self.MAX_LENGTH,tokenizer)
            model_input[i].append(ids_q)
            i+=1
            model_input[i].append(masks_q)
            i+=1
            model_input[i].append(segments_q)
            
        for xx in range((self.MAX_SENTENCES*3)+3):
            model_input[xx] = np.asarray(model_input[xx], dtype=np.int32)
            
        print(model_input[0].shape)
        return model_input

    def _print_evaluation_metrics(y_true, y_pred, label='', is_regression=True, label2=''):
        print('==================', label2)
        ### For regression
        if is_regression:
            print('mean_absolute_error',label,':', sklearn.metrics.mean_absolute_error(y_true, y_pred))
            print('mean_squared_error',label,':', sklearn.metrics.mean_squared_error(y_true, y_pred))
            print('r2 score',label,':', sklearn.metrics.r2_score(y_true, y_pred))
            #     print('max_error',label,':', sklearn.metrics.max_error(y_true, y_pred))
            return sklearn.metrics.mean_squared_error(y_true, y_pred)
        else:
            ### FOR Classification
    #         print('balanced_accuracy_score',label,':', sklearn.metrics.balanced_accuracy_score(y_true, y_pred))
    #         print('average_precision_score',label,':', sklearn.metrics.average_precision_score(y_true, y_pred))
    #         print('balanced_accuracy_score',label,':', sklearn.metrics.balanced_accuracy_score(y_true, y_pred))
    #         print('accuracy_score',label,':', sklearn.metrics.accuracy_score(y_true, y_pred))
            print('f1_score',label,':', sklearn.metrics.f1_score(y_true, y_pred))
            
            matrix = sklearn.metrics.confusion_matrix(y_true, y_pred)
            print(matrix)
            TP,TN,FP,FN = matrix[1][1],matrix[0][0],matrix[0][1],matrix[1][0]
            Accuracy = (TP+TN)/(TP+FP+FN+TN)
            Precision = TP/(TP+FP)
            Recall = TP/(TP+FN)
            F1 = 2*(Recall * Precision) / (Recall + Precision)
            print('Acc', Accuracy, 'Prec', Precision, 'Rec', Recall, 'F1',F1)
            return sklearn.metrics.accuracy_score(y_true, y_pred)

    def _evalPred(ypred, threhold):
        if ypred>threhold:
            print("joke is funny!")
            funny=True
        else:
            print("joke is not funny")
            funny=False
        return funny


    def _evalJoke(model, joke, tokenizer, columns=["text"]):
        X = pd.DataFrame([joke], columns=["text"])
        X = self._compute_input_arrays(X, columns=columns, tokenizer=tokenizer)
        ypred = model.predict(X)
        return ypred


def main():
    X = "I invented a new word!\nPlagiarism!"

    logger = logging.getLogger(__name__)
    logger.info("try infer from saved model experiment")

    model = HumourRecognitionModel()
    model.predict(X)


if __name__ == "__main__":
    main()
