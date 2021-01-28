import os
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from werkzeug.utils import secure_filename
from tensorflow.keras.preprocessing import image
import joblib
import pandas as pd 
import numpy as np 
import pandas as pd 
import mglearn



app = Flask(__name__)
app.config

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/model')
def model():    
    return render_template('model/model.html')

@app.route('/main')
def main():    
    return render_template('public/main.html')

if __name__ == '__main__':
    app.run(debug=True)    
