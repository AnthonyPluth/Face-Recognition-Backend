from face_rec_api.utils import ensure_directory
from libfaceid.detector import FaceDetector
from libfaceid.encoder import FaceEncoder
import cv2
import face_rec_api.config as config
import face_rec_api.image_processing as image_processing
import os


def get_dataset_names(file_path):
    for (_d, names, _f) in os.walk(file_path):
        return names
    return None


def train_recognition(verify):
    ensure_directory(config.INPUT_DIR_DATASET)

    names = get_dataset_names(config.INPUT_DIR_DATASET)
    if names is not None:
        for name in names:
            for (_d, _n, files) in os.walk(config.INPUT_DIR_DATASET + "/" + name):
                print(name + ": " + str(files))

    ensure_directory(config.INPUT_DIR_MODEL_TRAINING)
    face_detector = FaceDetector(model=config.detecting_model, path=config.INPUT_DIR_MODEL_DETECTING)
    face_encoder = FaceEncoder(model=config.encoding_model, path=config.INPUT_DIR_MODEL_ENCODING,
                               path_training=config.INPUT_DIR_MODEL_TRAINING, training=True)
    face_encoder.train(face_detector, path_dataset=config.INPUT_DIR_DATASET,
                       verify=verify, classifier=config.classifier_model)


def test_recognition():
    for subdir in os.listdir(config.INPUT_DIR_DATASET):
        subdir_path = config.INPUT_DIR_DATASET + '/' + subdir
        for filename in os.listdir(subdir_path):
            file_path = subdir_path + '/' + filename
            frame = cv2.imread(file_path)
            face_id, confidence = image_processing.identify_person(frame)
            print(face_id, confidence)


def prep_images():
    import config
    face_detector = FaceDetector(model=config.detecting_model,
                                 path=config.INPUT_DIR_MODEL_DETECTING)

    for subdir in os.listdir(config.INPUT_DIR_DATASET):
        subdir_path = config.INPUT_DIR_DATASET + '/' + subdir
        for filename in os.listdir(subdir_path):
            file_path = subdir_path + '/' + filename
            print(filename)
            if filename == '.DS_Store':
                delete_file(file_path, filename)

            frame = cv2.imread(file_path)

            if image_processing.frame_has_blur(frame):
                print(f'deleting {file_path} due to blur')
                delete_file(file_path, filename)
                continue

            faces = face_detector.detect(frame)
            if len(faces) != 1:
                # Delete images if we don't find exactlty one face
                print(f'deleting {file_path} due to number of faces')
                delete_file(file_path, filename)


def delete_file(file_path, filename):
    os.rename(file_path, 'DELETE/' + filename)


def run():
    prep_images()
    train_recognition(True)
    test_recognition()
    print("\nImage dataset training completed!")


if __name__ == '__main__':
    run()
