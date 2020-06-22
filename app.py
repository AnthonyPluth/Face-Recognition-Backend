# TODO: make image_processing functions async (again)
# TODO: switch to websockets?

from face_rec_api import image_processing
from face_rec_api import training
from fastapi import Path, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import tensorflow as tf

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class RequestBody(BaseModel):
    snapshot: str = None


@app.post("/identify")
async def find_faces_from_snapshot(request: RequestBody):
    img = image_processing.base64_to_numpy_array(request.snapshot)
    faces = image_processing.get_faces(img)

    bboxes = []
    for face in faces:
        (x, y, w, h) = face
        bboxes.append({"x": int(x), "y": int(y), "w": int(w), "h": int(h)})

    name, confidence = None, None
    if len(faces) > 0:
        cropped_img = image_processing.crop_frame(img, faces[0])
        name, confidence = image_processing.identify_person(cropped_img)

    return {"name": name, "confidence": confidence, "bounding_boxes": bboxes}


@app.post("/add_person/{name}")
async def add_new_person(
    request: RequestBody, name: str = Path(..., title="Name of new user")
):
    img = image_processing.base64_to_numpy_array(request.snapshot)
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
    return {"training status": "complete"}


@app.get("/status")
async def status():
    return {
        "status": "up",
        "tensorflowVersion": tf.__version__,
        "tensorflowGpu": len(tf.config.experimental.list_physical_devices("GPU")) > 0,
    }
