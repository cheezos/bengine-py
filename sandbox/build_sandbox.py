import os

os.system("python -m pip freeze > ../requirements.txt")
os.system("python ./setup.py build")
