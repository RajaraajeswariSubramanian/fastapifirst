from fastapi import FastAPI

app = FastAPI()

@app.get('/app')
def greeting():
      return {'greeting': 'Hello World'}