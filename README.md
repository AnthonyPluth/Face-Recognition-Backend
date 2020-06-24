# Face Recognition

## What it does
This package will allow you to train and run facial recognition using your computer's webcam.

## Prerequisites
- [ ] Python3.7+ and pip installed<br/>
    Mac:
    ```bash
    brew install python3
    curl -O https://bootstrap.pypa.io/get-pip.py
    python3 get-pip.py
    ```

    Windows: <br/>
    Install Python3.7+ by downloading the binary from [here](https://www.python.org/downloads/windows/) and running the binary file.

## Backend Setup
```bash
git clone https://gitlab.com/-/ide/project/abpluth/face-recognition-backend.git
cd face-recognition-backend
pip3 install -e .
```

## Running the API
```bash
uvicorn app:app --port 5000 --host 0.0.0.0
```

## Testing
Testing is done with tox and will automatically generate a code coverage report
```bash
tox
```
