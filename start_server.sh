#!/bin/bash
source /c/Users/Administrator/Documents/github/venv/face-recognition-backend/Scripts/activate
cd /c/Users/Administrator/Documents/github/face-recognition-backend/
uvicorn app:app --port 5000 --host 0.0.0.0
