from flask import Flask
from ml import ML
import asyncio

app = Flask(__name__)
ml = ML()


@app.route("/")
def hello_world():
  return "Hello world!"

@app.route("/run")
def run():
  # Run the ML program on a separate thread
  ml.run()
  return "Running"
  


