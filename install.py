import os

dependences = 'requirements.txt'

os.system('pip install virtualenv')
os.system('virtualenv venv')
os.system('source venv/bin/activate')
os.system('pip install -r {}'.format(dependences))