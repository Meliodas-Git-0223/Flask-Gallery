from flask import Flask, render_template,  flash, request, redirect, url_for
import os
from math import ceil
from werkzeug.utils import secure_filename
import use8

UPLOAD_FOLDER = 'static/images/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'webp'])


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
@app.route("/<int:pageNum>")
def home(pageNum = 1):
    if pageNum == None:
        pageNum = 1

    Elements = 30
    imagelist = os.listdir("./static/images/")

    elem = 1
    for file in imagelist:
        elem +=1
    
    pag = ceil(elem/Elements)
    
    imagelist = imagelist[(pageNum*Elements)-Elements:pageNum*Elements]
    imagess = {}
    for i in imagelist:
        imagess[i] = use8.decode(i.split(".")[0])
    return render_template('home.html', imagelist = imagess, pagesCount = pag)


@app.route('/img/<imagename>')
def imagepage(imagename):
	imagelist = os.listdir('./static/images/')
	for image in imagelist:
		if imagename in image:
			srcpic = image
	return render_template('image-show.html', srcpic = srcpic, imagename=imagename)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/upload" , methods = ["GET",'POST'])
def upload():
    if request.method == 'POST':
        name = request.form.get("Fname")
        encName = use8.encode(name)
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(encName + "."+ file.filename.split(".")[1])
            print(filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return render_template("Uploader.html")


@app.errorhandler(404)
def error_not_found(e):
    return render_template("not-found.html") , 404


if (__name__) == '__main__':
    app.run(host="0.0.0.0", port=8080)
