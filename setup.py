from setuptools import setup

requirements = [
    "faced @ git+https://github.com/iitzco/faced.git#egg=faced",
    "fastapi>=0.61.0",
    "imutils>=0.5.3",
    "numpy==1.18.5",
    "opencv-python>=4.1.0.25",
    "pillow>=8.1.2",
    "requests>=2.23.0",
    "tensorflow-gpu",
    "uvicorn>=0.11.5",
    "sklearn",
    "scipy",
]

tests_require = [
    "coverage>=5.1",
    "pytest>=4.6.11",
    "tox>=3.1.0",
    "WebTest>=1.3.1",
]

setup(
    name="face_rec_api",
    version=0.7,
    author="Anthony Pluth",
    author_email="abpluth@gmail.com",
    packages=["face_rec_api", "facenet", "libfaceid", "tests"],
    install_requires=requirements,
    tests_require=tests_require,
    zip_safe=False,
)
