from face_rec_api import image_processing
from face_rec_api import training
from flask import Flask, request
from flask_cors import CORS, cross_origin
import cv2
import json

app = Flask(__name__)
cors = CORS(app, support_credentials=True)


@app.route('/identify', methods=['POST', 'OPTIONS'])
@cross_origin()
def find_faces_from_snapshot():
    print(f'received {request.method} request on /identify endpoint')
    data = request.get_json()['body']
    encoded_image = json.loads(data)['snapshot']
    encoded_image = encoded_image.split(',')[1]

    img = image_processing.base64_to_numpy_array(encoded_image)
    faces = image_processing.get_faces(img)

    for face in faces:
        (x, y, w, h) = face
        cv2.rectangle(img, (x, y), (x + w, y + h), (36, 255, 12), 2)

    framed_img = image_processing.numpy_array_to_base64(img)

    name, confidence = None, None
    if len(faces) > 0:
        cropped_img = image_processing.crop_frame(img, faces[0])
        name, confidence = image_processing.identify_person(cropped_img)
    return {'framed_image': framed_img.decode('utf-8'), 'name': name, 'confidence': confidence}


@app.route('/add_person/<name>', methods=['POST', 'OPTIONS'])
@cross_origin()
def add_new_person(name):
    print(f'received {request.method} request on /add_person endpoint')
    data = request.get_json()['body']
    encoded_image = json.loads(data)['snapshot']
    encoded_image = encoded_image.split(',')[1]

    img = image_processing.base64_to_numpy_array(encoded_image)
    faces = image_processing.get_faces(img)
    if faces[0]:
        cropped_img = image_processing.crop_frame(img, faces[0])

        # save image
        image_processing.save_image(cropped_img, name)
    return {"status": 200}


@app.route('/train_model', methods=['GET', 'OPTIONS'])
@cross_origin()
def train_model():
    training.run()
    return {'training status': 'complete'}


@app.route('/health', methods=['GET', 'OPTIONS'])
@cross_origin()
def health_check():
    return {'status': 'up'}


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000, threaded=True)
