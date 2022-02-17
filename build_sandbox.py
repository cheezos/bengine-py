import os

os.system("python -m pip freeze > requirements.txt")
os.system("python ./sandbox/setup.py build")
