# Face Recognition
[![Build Status](https://gitlab.com/abpluth/hassio-face-recognition-consumer/badges/master/pipeline.svg)](https://gitlab.com/abpluth/hassio-face-recognition-consumer)
[![Coverage](https://gitlab.com/abpluth/hassio-face-recognition-consumer/badges/master/coverage.svg)](https://gitlab.com/abpluth/hassio-face-recognition-consumer)  

## Backend Setup
```bash
cd api
pip3 install -e .

# For testing, use:
pip3 install -e '.[testing]'
```

## Running the API
```bash
cd api
gunicorn --bind=0.0.0.0:5000 app:app
```


## Frontend Setup
```bash
cd frontend
yarn install
```

## Running the Frontend
```bash
cd frontend
yarn start
```

## How it works
This package will allow you to train and run facial recognition using your computer's webcam.
