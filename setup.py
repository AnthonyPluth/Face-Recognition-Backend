from setuptools import setup

requirements = [
    "facenet>=1.0.5",
    "fastapi>=",
    "imutils>=0.5.3",
    "numpy>=1.16.4",
    "opencv-python>=4.1.0.25",
    "requests>=2.23.0",
    "tensorflow==1.15.3",
    # if gpu is available, use:
    # "tensorflow-gpu==1.15.0",
    "uvicorn>=0.11.5",
    "deepface>=0.0.49"
]

tests_require = [
    "autohooks",
    "autohooks-plugins-black",
    "coverage>=5.1",
    "pytest>=4.6.11",
    "pytest-black>=0.3.9",
    "tox>=3.1.0",
    "WebTest>=1.3.1",
]

setup(
    name="face_rec_api",
    version=0.6,
    author="Anthony Pluth",
    author_email="abpluth@gmail.com",
    packages=["face_rec_api", "libfaceid", "tests"],
    install_requires=requirements,
    tests_require=tests_require,
    extras_require={"dev": ["autohooks", "autohooks-plugins-black"]},
    zip_safe=False,
)
