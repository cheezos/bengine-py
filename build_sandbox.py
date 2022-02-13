import os

def create_requirements() -> None:
    os.system("pip freeze > requirements.txt")

def build() -> None:
    create_requirements()

    os.system("python ./sandbox/setup.py build")

build()