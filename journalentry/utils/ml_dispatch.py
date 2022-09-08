from ml_kit.compiler import SUMMARIZER, SENTIMENT_PREDICTOR
import json

# def dispatch(text, ):
def populate_ml_fields(request_obj):
    if 'text' in request_obj.data:
        request_obj.data['sentiment'] = SENTIMENT_PREDICTOR(request_obj.data['text'])
        request_obj.data['summary'] = SUMMARIZER(request_obj.data['text'])
    return request_obj