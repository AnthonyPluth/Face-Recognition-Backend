from libfaceid.encoder import FaceEncoderModels
from libfaceid.detector import FaceDetectorModels
from libfaceid.classifier import FaceClassifierModels

INPUT_DIR_MODEL_DETECTING = "models/detection/"
INPUT_DIR_MODEL_ENCODING = "models/encoding/"
INPUT_DIR_MODEL_TRAINING = "models/training/"
INPUT_DIR_DATASET = "datasets"

detecting_model = FaceDetectorModels.FACENET
encoding_model = FaceEncoderModels.FACENET
classifier_model = FaceClassifierModels.RBF_SVM

min_confidence = 90
min_width_to_save = 50
save_all_faces = True
