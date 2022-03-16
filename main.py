from flask import Flask
from lesson import lesson
from date import date
from weather import weather

app = Flask(__name__)

@app.route("/")
def hello_world():
  return date()+". "+weather()+". "+lesson()+". "

app.run(host="0.0.0.0", port=8080)

