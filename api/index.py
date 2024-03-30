# from flask import Flask

# app = Flask(__name__)

# @app.route('/func/')
# def home():
#     return 'Hello, World!'

# @app.route('/func/about')
# def about():
#     return 'About'
# 通过unicorn启动时传一个参数是否套一层/api路由
from fastapi import FastAPI

app = FastAPI()

@app.get("/api/python")
def hello_world():
    return {"message": "Hello World"}