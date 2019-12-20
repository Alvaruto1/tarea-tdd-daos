import os

dependences = 'requirements.txt'

os.system('pip install virtualenv')
os.system('virtualenv venv')
os.system('. venv/bin/activate; pip install -r {}'.format(dependences))
