import time
import os

from scripts import status
from scripts import net
from scripts import debug

loginUrl = "https://discordapp.com/api/auth/login"

def loginForm():
    os.system('cls')
    print("Enter credentials below...\n")

    _email = input("Email: ")
    _pass = input("Password: ")

    doLogin(_email, _pass)

def doLogin(mail, password):
    _email = mail
    _pass = password

    if (_email == ""):
        debug.error(-1, "Email can not be empty")
    elif (_pass == ""):
        debug.error(-2, "Password can not be empty")
    else:
        os.system('cls')
        postData = "{\"email\":\""+ _email + "\" , \"password\":\""+ _pass + "\"}"

        debug.log(postData)

        net.discordPostData(loginUrl, postData, "")

        if (net.discordPostData == 200):
            debug.log("Succesfull login request, code: " + str(net.discordPostData))
        else:
            debug.error(-2, "Login failed, code: " + str(net.discordPostData))
        

