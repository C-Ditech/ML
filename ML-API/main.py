# README
# Hello everyone, in here I (Kaenova | Bangkit Mentor ML-20) 
# will give you some headstart on createing ML API. 
# Please read every lines and comments carefully. 
# 
# I give you a headstart on text based input and image based input API. 
# To run this server, don't forget to install all the libraries in the
# requirements.txt simply by "pip install -r requirements.txt" 
# and then use "python main.py" to run it
# 
# For ML:
# Please prepare your model either in .h5 or saved model format.
# Put your model in the same folder as this main.py file.
# You will load your model down the line into this code. 
# There are 2 option I give you, either your model image based input 
# or text based input. You need to finish functions "def predict_text" or "def predict_image"
# 
# For CC:
# You can check the endpoint that ML being used, eiter it's /predict_text or 
# /predict_image. For /predict_text you need a JSON {"text": "your text"},
# and for /predict_image you need to send an multipart-form with a "uploaded_file" 
# field. you can see this api documentation when running this server and go into /docs
# I also prepared the Dockerfile so you can easily modify and create a container iamge
# The default port is 8080, but you can inject PORT environement variable.
# 
# If you want to have consultation with me
# just chat me through Discord (kaenova#2859) and arrange the consultation time
#
# Share your capstone application with me! 🥳
# Instagram @kaenovama
# Twitter @kaenovama
# LinkedIn /in/kaenova

## Start your code here! ##

import os
import uvicorn
import traceback
import tensorflow as tf
import numpy as np
# import files
# import files
from pydantic import BaseModel
from urllib.request import Request
from fastapi import FastAPI, Response, UploadFile
from utils import load_image_into_numpy_array
from PIL import Image


# Initialize Model
# If you already put yout model in the same folder as this main.py
# You can load .h5 model or any model below this line

# If you use h5 type uncomment line below
model = tf.keras.models.load_model('./chicken_disease.h5')
# If you use saved model type uncomment line below
# model = tf.saved_model.load("./my_model_folder")
path_file = os.getcwd()
class_names = ['cocci', 'healthy', 'ncd', 'salmonella']

app = FastAPI()

# This endpoint is for a test (or health check) to this server
@app.get("/")
def index():
    # return os.getcwd()
    return "Hello world from ML endpoint!"

# If your model need text input use this endpoint!
class RequestText(BaseModel):
    text:str

@app.post("/predict_text")
def predict_text(req: RequestText, response: Response):
    try:
        # In here you will get text sent by the user
        text = req.text
        print("Uploaded text:", text)
        
        # Step 1: (Optional) Do your text preprocessing
        
        # Step 2: Prepare your data to your model
        
        # Step 3: Predict the data
        # result = model.predict(...)
        
        # Step 4: Change the result your determined API output
        
        return "Endpoint not implemented"
    except Exception as e:
        traceback.print_exc()
        response.status_code = 500
        return "Internal Server Error"

# If your model need image input use this endpoint!
@app.post("/predict_image")
def predict_image(uploaded_file: UploadFile, response: Response):
    try:
        # Checking if it's an image
        if uploaded_file.content_type not in ["image/jpeg", "image/png"]:
            response.status_code = 400
            return "File is not an image"
        
        # Save the uploaded file
        file_path = f"./{uploaded_file.filename}"
        with open(file_path, "wb") as f:
            f.write(uploaded_file.file.read())
        
        # Load and preprocess the image
        image = tf.keras.utils.load_img(path=file_path, target_size=(224, 224))
        input_arr = tf.keras.utils.img_to_array(image)
        input_arr = np.array([input_arr])

        # Predict the data
        predictions = model.predict(input_arr)
        predicted_index = np.argmax(predictions)
        predicted_name = class_names[predicted_index]
        percentage = round(predictions[0][predicted_index] * 100, 2)

        # Remove the temporary file
        os.remove(file_path)

        # Change the result to your determined API output
        return predicted_name,percentage
    
    except Exception as e:
        traceback.print_exc()
        response.status_code = 500
        return "Internal Server Error"


# Starting the server
# Your can check the API documentation easily using /docs after the server is running
port = os.environ.get("PORT", 8080)
print(f"Listening to http://0.0.0.0:{port}")
uvicorn.run(app, host='0.0.0.0',port=port)