from flask import Flask, render_template, request
import os
from run_code import detect
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/start", methods=['GET', 'POST'])
def index():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('Start') == 'Start':
            # pass
            detect()
            return render_template("index.html")
    else:
        # pass # unknown
        return render_template("index.html")

if __name__ == '__main__':
   app.run()
