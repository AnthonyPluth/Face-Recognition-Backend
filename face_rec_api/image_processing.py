from libfaceid.encoder import FaceEncoder
from faced import FaceDetector
import base64
import cv2
import face_rec_api.config as config
import face_rec_api.utils as utils
import numpy as np
import time

face_detector = FaceDetector()
face_encoder = FaceEncoder(
    model=config.encoding_model,
    path=config.INPUT_DIR_MODEL_ENCODING,
    path_training=config.INPUT_DIR_MODEL_TRAINING,
    training=False,
)


async def get_faces(frame):
    bboxes = face_detector.predict(frame, 0.8)
    return bboxes


async def crop_frame(frame, face):
    (x, y, w, h) = face
    return frame[y: y + h, x: x + w]


async def frame_has_blur(frame):
    # compute the Laplacian of the image and then return the focus
    # measure, which is simply the variance of the Laplacian
    blur = cv2.Laplacian(frame, cv2.CV_64F).var()
    return blur < 100


async def base64_to_numpy_array(encoded_image):
    try:
        raw = encoded_image.split(",")[1]
    except Exception:
        raw = encoded_image
    nparr = np.frombuffer(base64.b64decode(raw), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img


async def numpy_array_to_base64(image):
    _, bytes_image = cv2.imencode(".webp", image)
    base64_image = "data:image/webp;base64," + base64.b64encode(bytes_image).decode(
        "utf-8"
    )
    return base64_image


async def identify_person(cropped):
    face_id, confidence = face_encoder.identify(cropped)
    return face_id, confidence


async def save_image(image, directory, filename=None):
    if not filename:
        filename = f"{time.time()}.webp"
    utils.ensure_directory(f"datasets/{directory}/")
    save_path = f"datasets/{directory}/{filename}"
    cv2.imwrite(save_path, image)
