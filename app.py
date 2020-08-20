from face_rec_api import image_processing
from face_rec_api import training
from fastapi import File, Path, FastAPI, WebSocket, Request, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import tensorflow as tf

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["192.168.0.0/16"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


async def get_faces(img):
    bboxes = []
    faces = image_processing.get_faces(img)

    for face in faces:
        (x, y, w, h) = face
        bboxes.append({"x": int(x), "y": int(y), "w": int(w), "h": int(h)})

    return faces, bboxes


async def detect_faces(snapshot):
    img = image_processing.base64_to_numpy_array(snapshot)
    faces, bboxes = get_faces(img)

    return bboxes


async def recognize_faces(snapshot: str):
    img = image_processing.base64_to_numpy_array(snapshot)
    faces, bboxes = get_faces(img)

    name, confidence = None, None
    if len(faces) > 0:
        cropped_img = image_processing.crop_frame(img, faces[0])
        name, confidence = image_processing.identify_person(cropped_img)

    return {"name": name, "confidence": confidence, "bounding_boxes": bboxes}


async def register_face(name, snapshot):
    img = image_processing.base64_to_numpy_array(snapshot)
    faces, bboxes = get_faces(img)

    if faces[0]:
        cropped_img = image_processing.crop_frame(img, faces[0])
        # save image
        image_processing.save_image(cropped_img, name)

    return bboxes


@app.post("/face/detect")
async def detect_faces_post(image: list = Form(...)) -> dict:
    img = await image[0].read()
    return await detect_faces(img)


@app.post("/face/recognize")
async def recognize_faces_post(image: list = Form(...)) -> dict:
    img = await image[0].read()
    return await recognize_faces(img)


@app.post("/face/register")
async def register_face(name: str, image: list = Form(...)) -> dict:
    img = await image[0].read()
    return await register_face(name, img)


@app.get("/train_model")
async def train_model():
    training.run()
    # reload encoder with new data

    return {"training status": "complete"}


@app.websocket("/")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_json()
        request_type = list(data.keys())[0]

        if request_type == "identify":
            await recognize_faces(data["identify"])
        elif request_type == "record":
            name = request_json["name"]
            snapshot = request_json["snapshot"]
            bboxes = await register_face(name, snapshot)
            return {"name": "RECORDING...", "confidence": 0.00, "bboxes": bboxes}


# if __name__ == "__main__":
#     import cv2
#
#     cap = cv2.VideoCapture(0)
#
#     while True:
#         ret, img = cap.read()
#         print(img.shape)
#         faces = image_processing.get_faces(img)
#
#         bboxes = []
#         for face in faces:
#             (x, y, w, h) = face
#             bboxes.append({"x": int(x), "y": int(y), "w": int(w), "h": int(h)})
#
#         name, confidence = None, None
#         if len(faces) > 0:
#             cropped_img = image_processing.crop_frame(img, faces[0])
#             name, confidence = image_processing.identify_person(cropped_img)
#
#         print(name, confidence)
