from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    imagelist = os.listdir("./static/images/")
    print(imagelist)
    return render_template('home.html', imagelist = imagelist)

@app.errorhandler(404)
def error_not_found(e):
    return render_template("not-found.html") , 404


if (__name__) == '__main__':
    app.run(host="0.0.0.0", port=8080)
