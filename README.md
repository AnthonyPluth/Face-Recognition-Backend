# Face Recognition

## Prerequisites
- [ ] Python3.7+ and pip installed
```bash
brew install python3
curl -O https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py

## Backend Setup
```bash
pip3 install -e .
```

## Running the API
```bash
uvicorn app:app --port 5000 --host 0.0.0.0
```

## How it works
This package will allow you to train and run facial recognition using your computer's webcam.
