
import uvicorn
from fastapi import FastAPI

from model import SentimentModel, SentimentQueryModel

app = FastAPI()

model = SentimentModel()

@app.post('/predict')
def predict(data: SentimentQueryModel):
    print('call predict')
    data = data.dict()
    
    polarity, subjectivity = model.get_sentiment(data['text'])

    return {'polartiy':polarity,
            'subjectivity':subjectivity}


if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=7000)
