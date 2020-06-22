from setuptools import setup

requirements = [
    'facenet>=1.0.5',
    'fastapi>='
    'imutils>=0.5.3',
    'numpy>=1.16.4',
    'opencv-python>=4.1.0.25',
    'requests>=2.23.0',
    # 'tensorflow==1.15.0',
    'tensorflow-gpu==1.15.0',
    'uvicorn>=0.11.5',
]

tests_require = [
    'coverage>=5.1',
    'pytest >= 4.6.11',
    'tox>=3.1.0',
    'WebTest >= 1.3.1',
]

setup(
    name='face_rec_api',
    version=0.6,
    author='Anthony Pluth',
    author_email='abpluth@gmail.com',
    packages=['face_rec_api', 'libfaceid', 'tests'],
    install_requires=requirements,
    tests_require=tests_require,
    zip_safe=False,
)
