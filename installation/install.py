import os,platform

dependences = 'requirements.txt'

os.system('pip install virtualenv')
os.system('virtualenv venv')

commandOS = 'venv/Scripts/activate.bat' if platform.system() == 'Windows' else '. venv/bin/activate'

os.system('{}; pip install -r {}'.format(commandOS,dependences))
