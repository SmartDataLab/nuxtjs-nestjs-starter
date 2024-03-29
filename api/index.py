# from flask import Flask

# app = Flask(__name__)

# @app.route('/func/')
# def home():
#     return 'Hello, World!'

# @app.route('/func/about')
# def about():
#     return 'About'

from fastapi import FastAPI

app = FastAPI()

@app.get("/api/python")
def hello_world():
    return {"message": "Hello World"}