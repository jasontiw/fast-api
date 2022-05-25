## Access to Env
``` 
.\venv\Scripts\activate
```
## Run
``` 
uvicorn main:app --reload 
```
## Run Test
``` 
pytest
```
## Documentation

 - http://127.0.0.1:8000/docs
 - http://127.0.0.1:8000/redoc

# how create a new project 

## configure the project 

```bash
py -m venv venv

.\venv\Scripts\activate

pip freeze > requirements.txt

pip install fastapi uvicorn requests pytest
```


## hello world
main.py
``` python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {'Hello':'World'} 
```