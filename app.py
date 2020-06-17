from face_rec_api import image_processing
from face_rec_api import training
from flask import Flask, request
from flask_cors import CORS, cross_origin
import cv2
import json
import tensorflow as tf

app = Flask(__name__)
CORS(app)
# TODO: make image_processing functions async (again)
# TODO: switch to FastAPI/starlette.io/web2py/Pyramid/Tornado/sanic for async server
# TODO: add endpoint to restart api (in order to load newly trained model)


@app.route('/identify', methods=['POST', 'OPTIONS'])
@cross_origin()
def find_faces_from_snapshot():
    print(f'received {request.method} request on /identify endpoint')
    data = request.get_json()['body']
    encoded_image = json.loads(data)['snapshot']

    img = image_processing.base64_to_numpy_array(encoded_image)
    faces = image_processing.get_faces(img)

    for face in faces:
        (x, y, w, h) = face
        cv2.rectangle(img, (x, y), (x + w, y + h), (36, 255, 12), 2)

    name, confidence = None, None
    if len(faces) > 0:
        cropped_img = image_processing.crop_frame(img, faces[0])
        name, confidence = image_processing.identify_person(cropped_img)
        encoded_image = image_processing.numpy_array_to_base64(img)

    return {'framed_image': encoded_image.split(',')[1], 'name': name, 'confidence': confidence}


@app.route('/add_person/<name>', methods=['POST', 'OPTIONS'])
@cross_origin()
def add_new_person(name):
    print(f'received {request.method} request on /add_person endpoint')
    data = request.get_json()['body']
    encoded_image = json.loads(data)['snapshot']

    img = image_processing.base64_to_numpy_array(encoded_image)
    faces = image_processing.get_faces(img)
    if faces[0]:
        cropped_img = image_processing.crop_frame(img, faces[0])
        (x, y, w, h) = faces[0]
        cv2.rectangle(img, (x, y), (x + w, y + h), (36, 255, 12), 2)
        framed_img = image_processing.numpy_array_to_base64(img)

        # save image
        image_processing.save_image(cropped_img, name)

    return {'framed_image': framed_img}


@app.route('/train_model', methods=['GET', 'OPTIONS'])
@cross_origin()
def train_model():
    training.run()
    return {'training status': 'complete'}


@app.route('/status', methods=['GET', 'OPTIONS'])
@cross_origin()
def status():
    # return {'status': 'up', 'tensorflowVersion': tf.__version__, 'tensorflowGpu': len(tf.config.experimental.list_physical_devices('GPU'))>0}
    return {'status': 'up', 'tensorflowVersion': tf.__version__, 'tensorflowGpu': True}
