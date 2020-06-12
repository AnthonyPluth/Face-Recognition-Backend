# Face Recognition

## Prerequisites
- [ ] Python3.7+ and pip installed
```bash
brew install python3
curl -O https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py
```
- [ ] generate self-signed certs in the certs directory:
```bash
openssl req -newkey rsa:2048 -nodes -keyout certs/key.pem -x509 -days 365 -out certs/certificate.pem
```

## Backend Setup
```bash
pip3 install -e .
```

## Running the API
```bash
gunicorn -c gunicorn.conf.py app:app
```

## How it works
This package will allow you to train and run facial recognition using your computer's webcam.
