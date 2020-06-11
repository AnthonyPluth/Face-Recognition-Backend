# Face Recognition

## Prerequisites
- [ ] Python3.7 or greater installed

## Backend Setup
```bash
pip3 install -e .
```

## Running the API
```bash
gunicorn --bind=0.0.0.0:5000 app:app
```

## How it works
This package will allow you to train and run facial recognition using your computer's webcam.
