from libfaceid.encoder import FaceEncoderModels
from libfaceid.detector import FaceDetectorModels
from libfaceid.classifier import FaceClassifierModels

INPUT_DIR_MODEL_DETECTING = "face_rec_api/models/detection/"
INPUT_DIR_MODEL_ENCODING = "face_rec_api/models/encoding/"
INPUT_DIR_MODEL_TRAINING = "face_rec_api/models/training/"
INPUT_DIR_DATASET = "datasets"

detecting_model = 'DeepFace'

min_confidence = 90
min_width_to_save = 50
save_all_faces = True
