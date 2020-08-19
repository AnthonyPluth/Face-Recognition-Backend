# TODO: make image_processing functions async (again)

from face_rec_api import image_processing
from face_rec_api import training
from fastapi import Path, FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


async def find_faces_from_snapshot(snapshot):
    img = image_processing.base64_to_numpy_array(snapshot)
    faces = image_processing.get_faces(img)

    bboxes = []
    for face in faces:
        (x, y, w, h) = face
        bboxes.append({"x": int(x), "y": int(y), "w": int(w), "h": int(h)})

    name, confidence = None, None
    if len(faces) > 0:
        cropped_img = image_processing.crop_frame(img, faces[0])
    #     name, confidence = image_processing.identify_person(cropped_img)
    #
    return {"name": name, "confidence": confidence, "bounding_boxes": bboxes}


async def add_new_person(request_json):
    name = request_json["name"]
    snapshot = request_json["snapshot"]

    img = image_processing.base64_to_numpy_array(snapshot)
    faces = image_processing.get_faces(img)

    bboxes = []
    for face in faces:
        (x, y, w, h) = face
        bboxes.append({"x": int(x), "y": int(y), "w": int(w), "h": int(h)})

    if faces[0]:
        cropped_img = image_processing.crop_frame(img, faces[0])
        # save image
        image_processing.save_image(cropped_img, name)

    return {"name": "RECORDING...", "confidence": 0.00, "bboxes": bboxes}


@app.get("/train_model")
async def train_model():
    training.run()
    # reload encoder with new data

    return {"training status": "complete"}


@app.get("/status")
async def status():
    return {
        "status": "up",
    }


@app.websocket("/")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_json()
        request_type = list(data.keys())[0]

        if request_type == "identify":
            await find_faces_from_snapshot(data["identify"])
        elif request_type == "record":
            await add_new_person(data["record"])