import os,platform

# get os
system = platform.system()
isWindows = system == 'Windows'

# file dependeces
dependences = 'installation\\requirements.txt' if isWindows else 'installation/requirements.txt'

# install virtualven and creation ven
os.system('pip install virtualenv')
os.system('virtualenv venv')

# activate env
commandOS = 'venv\\Scripts\\activate.bat' if platform.system() == 'Windows' else '. venv/bin/activate'

# join comands
join = '&' if isWindows else ';'

# install requirementes with pip
os.system('{} {} pip install -r {}'.format(commandOS,join,dependences))
