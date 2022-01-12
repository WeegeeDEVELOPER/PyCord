import time

from scripts import status

from scripts import login

def __mainLoop__():

    if(status.loginForm):
        login.loginForm()

    time.sleep(0.15)

    __mainLoop__()

__mainLoop__()