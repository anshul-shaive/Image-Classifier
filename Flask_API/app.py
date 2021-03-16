# app.py
from flask import Flask, request, jsonify
import tensorflow as tf
from PIL import Image
import base64
import io
import numpy as np
import cv2

# app = Flask(__name__)
app = Flask(__name__,static_url_path='/static')

dog_classifer_model = tf.keras.models.load_model('static/dog_classifier_model.h5')

num_to_classes={0: 'malamute',
 1: 'doberman',
 2: 'french_bulldog',
 3: 'beagle',
 4: 'saint_bernard',
 5: 'tibetan_mastiff',
 6: 'golden_retriever',
 7: 'scottish_deerhound',
 8: 'pug',
 9: 'chihuahua'}

@app.route('/get_prediction/', methods=['GET'])
def respond():
    return jsonify({'Response':'Use post route of same name and pass image in base64 format'})

@app.route('/get_prediction/', methods=['POST'])
def dog_classifer():
    image = request.form.get('image')
    imgdata = base64.b64decode(image)
    image_dec = Image.open(io.BytesIO(imgdata))
    image_dec.save('static/out.jpg','JPEG')
    np_image = np.zeros((1, 224, 224, 3), dtype=np.uint8)
    np_image[0] = cv2.resize(cv2.imread('static/out.jpg'), (224, 224))
    np_image = np.expand_dims(np_image[0], axis=0)
    preprocess_input = tf.keras.applications.resnet50.preprocess_input
    np_image=preprocess_input(np_image)
    prediction=dog_classifer_model.predict(np_image)[0]
    print(prediction)
    max_index=np.argmax(prediction)
    score=prediction[max_index]
    breed=num_to_classes.get(max_index)
    return jsonify({'breed':breed,'score':str(score)})

@app.route('/')
def index():
    return "<h1>Use get_prediction post route and pass a base64 image in 'image' parameter</h1>"

if __name__ == '__main__':
    app.run(threaded=True, port=5000)