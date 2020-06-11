from setuptools import setup

requirements = [
    'facenet>=1.0.5',
    'imutils>=0.5.3',
    'numpy>=1.16.4',
    'opencv-python>=4.1.0.25',
    'requests>=2.23.0',
    'coverage>=5.1',
    'tensorflow==1.15.3',
]

tests_require = [
    'WebTest >= 1.3.1',
    'pytest >= 4.6.11',
]

setup(
    name='face_rec_api',
    version=0.5,
    author='Anthony Pluth',
    author_email='abpluth@gmail.com',
    packages=['face_rec_api', 'libfaceid', 'tests'],
    install_requires=requirements,
    tests_require=tests_require,
    zip_safe=False,
)
