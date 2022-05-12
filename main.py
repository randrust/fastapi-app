from unicodedata import name
import fastapi
import uvicorn


app = fastapi.FastAPI()


@app.get('/')
def index():
    return {'message':'Hellow world!'}

if __name__ == '__main__':
    uvicorn.run(app)