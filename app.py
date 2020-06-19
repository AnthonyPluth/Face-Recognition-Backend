from face_rec_api import image_processing
from face_rec_api import training
from flask import Flask, request
from flask_cors import cross_origin
import cv2
import json
import tensorflow as tf

app = Flask(__name__)

# TODO: make image_processing functions async (again)
# TODO: switch to sanic/bottle/aiohttp/vibora for async server
# TODO: switch to websockets?


@app.route('/identify', methods=['POST', 'OPTIONS'])
@cross_origin()
def find_faces_from_snapshot():
    print(f'received {request.method} request on /identify endpoint')
    data = request.get_json()['body']
    encoded_image = json.loads(data)['snapshot']

    img = image_processing.base64_to_numpy_array(encoded_image)
    faces = image_processing.get_faces(img)

    bboxes = []
    for face in faces:
        (x, y, w, h) = face
        bboxes.append({"x": x, "y": y, "w": w, "h": h})

    name, confidence = None, None
    if len(faces) > 0:
        cropped_img = image_processing.crop_frame(img, faces[0])
        name, confidence = image_processing.identify_person(cropped_img)

    return {'name': name, 'confidence': confidence, "bboxes": bboxes}


@app.route('/add_person/<name>', methods=['POST', 'OPTIONS'])
@cross_origin()
def add_new_person(name):
    print(f'received {request.method} request on /add_person endpoint')
    data = request.get_json()['body']
    encoded_image = json.loads(data)['snapshot']

    img = image_processing.base64_to_numpy_array(encoded_image)
    faces = image_processing.get_faces(img)
    bboxes = []
    for face in faces:
        (x, y, w, h) = face
        bboxes.append({"x": x, "y": y, "w": w, "h": h})

    if faces[0]:
        cropped_img = image_processing.crop_frame(img, faces[0])

        # save image
        image_processing.save_image(cropped_img, name)

    return {'bboxes': bboxes}


@app.route('/train_model', methods=['GET', 'OPTIONS'])
@cross_origin()
def train_model():
    print(f'received {request.method} request on /train_model endpoint')
    training.run()
    return {'training status': 'complete'}


@app.route('/status', methods=['GET', 'OPTIONS'])
@cross_origin()
def status():
    print(f'received {request.method} request on /status endpoint')
    return {'status': 'up', 'tensorflowVersion': tf.__version__, 'tensorflowGpu': len(tf.config.experimental.list_physical_devices('GPU')) > 0}


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=rue, port=5000, threaded=rue)
