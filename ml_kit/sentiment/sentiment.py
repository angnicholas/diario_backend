from transformers import AutoModelForSequenceClassification
from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer
import numpy as np
from scipy.special import softmax
import csv
import urllib.request
from typing import List

#git clone https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment
#Then put inside the following folder
HANDLE = 'ml_kit/sentiment/twitter-roberta-base-sentiment'
SENTENCE_SEPARATOR = '. '
MAX_MODEL_LEN = 512

class SentimentPredictor():

    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(HANDLE)
        self.model = AutoModelForSequenceClassification.from_pretrained(HANDLE)
        self.labels = ['negative', 'neutral', 'positive']

    # Preprocess text (username and link placeholders)
    @staticmethod
    def preprocess(text):
        new_text = []   
    
        for t in text.split(" "):
            t = '@user' if t.startswith('@') and len(t) > 1 else t
            t = 'http' if t.startswith('http') else t
            new_text.append(t)
        return " ".join(new_text)

    def __call__(self, text:str) -> dict:
        # sentences = text.split(SENTENCE_SEPARATOR)

        # does average sentiment

        text = self.preprocess(text)
        sentences = text.split(SENTENCE_SEPARATOR)
        encoded_input = self.tokenizer(
            sentences, 
            padding=True,
            return_tensors='pt', 
            truncation=True, 
            max_length=MAX_MODEL_LEN
        )
        output = self.model(**encoded_input)
        scores = output[0].detach().numpy()
        softmaxed = softmax(scores, axis=1)    
        averaged_scores = np.mean(softmaxed, axis=0)
        return {l:float(s) for l,s  in zip(self.labels, averaged_scores)}


