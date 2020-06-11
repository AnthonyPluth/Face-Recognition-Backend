# Face Recognition

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

## How it works
This package will allow you to train and run facial recognition using your computer's webcam.
