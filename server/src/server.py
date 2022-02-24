from flask import Flask
from flask_cors import CORS
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from cluster import create_cluster


app = Flask(__name__)
CORS(app)
@app.route("/")
def home():
    return create_cluster()
    
if __name__ == "__main__":
    app.run(debug=True)