import cloudpickle
import torch
import LSTM_model
from flask import Flask, render_template, request

app=Flask(__name__)

index="index.html"

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", title="aa", message="fuck")

@app.route("/", methods=["POST"])
def form():
    with open('model.pkl', 'rb') as f:
        model = cloudpickle.load(f)
    field=request.form["field"]
    maked_words = LSTM_model.generate_seq(model, start_phase=field, length=10)
    return render_template("index.html", title="Index with Jinja", message=f"Hello{maked_words}")