from flask import Flask, render_template
from requests import request
import pandas as pd

app=Flask(__name__)

@app.route('/')
def main():
    return render_template("main.html")

@app.route('/confirm',methods=['GET'])
def intimate():
    return render_template("intimate.html" )


if __name__=="__main__":
    app.run(debug=True)
