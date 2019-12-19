import os

dependences = 'requirements.txt'

os.system('pip install virtualenv')
os.system('virtualenv venv')

variables = """export FLASK_APP="run.py"
export SECRET="some-very-long-string-of-random-characters-CHANGE-TO-YOUR-LIKING"
export APP_SETTINGS="development"
"""

os.system("echo '{}' > .env".format(variables))
os.system('. venv/bin/activate; pip install -r {}'.format(dependences))
