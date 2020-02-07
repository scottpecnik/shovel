from shovel import task
import os

os.environ['SHELL'] = 'tcsh'

@task
def sourceCard():
    '''Source yubikey'''
    os.system("""gpg-agent --killall""")
    os.system("""source ~/.zshrc""")

@task
def editCard():
    '''Edit yubikey card'''
    os.system("""gpg --card-edit""")
