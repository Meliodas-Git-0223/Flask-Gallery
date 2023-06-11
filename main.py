from flask import Flask, render_template
import os
from math import ceil

app = Flask(__name__)

@app.route('/')
@app.route("/<int:pageNum>")
def home(pageNum):
    Elements = 30
    imagelist = os.listdir("./static/images/")

    elem = 1
    for file in imagelist:
        elem +=1
    
    pag = ceil(elem/Elements)
    
    imagelist = imagelist[(pageNum*Elements)-Elements:pageNum*Elements]
    print(imagelist)
    return render_template('home.html', imagelist = imagelist, pagesCount = pag)


@app.route('/img/<imagename>')
def imagepage(imagename):
	imagelist = os.listdir('./static/images/')
	for image in imagelist:
		if imagename in image:
			srcpic = image
	return render_template('image-show.html', srcpic = srcpic, imagename=imagename)

@app.errorhandler(404)
def error_not_found(e):
    return render_template("not-found.html") , 404


if (__name__) == '__main__':
    app.run(host="0.0.0.0", port=8080)
