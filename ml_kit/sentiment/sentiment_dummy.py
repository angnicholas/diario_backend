class DummySentimentPredictor():

    def __init__(self):
        pass

    def __call__(self, text: str) -> dict:

        return {
            'positive': 0.99,
            'neutral': 0.99,
            'negative': 0.99,
        }
