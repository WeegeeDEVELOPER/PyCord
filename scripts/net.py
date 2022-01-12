import requests
import time
import pycurl
import certifi

from io import BytesIO
from urllib.parse import urlencode
from requests.api import head

from scripts import status
from scripts import debug

def discordPostData(url, postData, authToken):
    authHead = "Authorization: " + str(authToken)
    contentLength = "Content-Length: " + postData

    b_obj = BytesIO()
    crl = pycurl.Curl()

    if (crl):
        crl.setopt(crl.CAINFO, certifi.where())
        crl.setopt(crl.URL, url)
        crl.setopt(crl.HEADERFUNCTION, debug.display_header)
        crl.setopt(crl.WRITEDATA, b_obj)
        crl.perform()
        crl.close()
        debug.log(debug.headers)
        


    r = requests.get(url)

    debug.log("post data: " + str(postData))
    debug.log("status code: " + str(r.status_code))

    return r.status_code


    