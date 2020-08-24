import os
from flask import Flask, render_template, request
import cv2
import base64
from Model.load_model import Loader

global model

load_model = Loader()
os.chdir("./Model")
model = load_model.load()
os.chdir("../")

app = Flask(__name__)


def convertimage(imgstring):
    imgdata = base64.b64decode(imgstring)
    filename = 'output.jpeg'
    with open(filename, 'wb') as f:
        f.write(imgdata)


# 23

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():
    imagestr = str(request.get_data())

    convertimage(imgstring=imagestr.split(',')[1])
    x = cv2.imread(os.getcwd() + "/output.jpeg", 1)

    if x is None:
        os.remove("output.jpeg")
        return "No image was uploaded!!"

    resized = cv2.resize(x, (224, 224), interpolation=cv2.INTER_AREA)
    resized = resized.reshape(1, 224, 224, 3)
    resized = resized / 255
    prediction = model.predict(resized)

    os.remove("output.jpeg")

    if prediction[0] > 0.5:
        return "dog"
    else:
        return "cat"


def main():
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port)


if __name__ == "__main__":
    main()
