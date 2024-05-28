# 1. library import 

import uvicorn ## ASGI (Asynchronous Server Gateway Interface)  It allows Falcon and other Python web frameworks to work with asynchronous web servers and take advantage of asynchronous programming techniques. Synchronous Processing. ASGI is an asynchronous protocol, which means that it allows parallel processing of multiple requests.
from fastapi import FastAPI
from StudentsResult import StudentResult
import numpy as np
import pandas as pd
import pickle

# 2. Create the app object

app = FastAPI()
pickle_in = open("model.pkl","rb")
model = pickle.load(pickle_in)

# 3. Index route, open automatically on http://127.0.0.1:8000

@app.get('/')
def index():
    return{'message':'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message located at: http://127.0.0.1:8000/AnyNameHere

@app.get('/{name}')
def get_name(name: str):
    return {'message': f'Hello, {name}'}

# 5. Expose the prediction functionality, make a prediction from the passed JSON data and return the predicted Student Placement with the confidence

@app.post('/predict')
def student_placement(data: StudentResult):
    data = data.dict()
    cgpa = data['cgpa']
    iq = data['iq']
    prediction = model.predict([[cgpa,iq]])
    if(prediction[0] == 1):
        prediction = "Congratulations! Based on the provided CGPA and IQ, the model predicts that the student will be placed."
    else:
        prediction = "Unfortunately, based on the provided CGPA and IQ, the model predicts that the student will not be placed."
    return{
        'prediction': prediction
    }

# 6. Run the API with uvicorn
# Will run on http://127.0.0.1.8000

if __name__ == '__main__':
    uvicorn.run(app,host='127.0.0.1', port=8000)

# uvicorn app:app --reload (run with this command) or python -m uvicorn app:app --reload
