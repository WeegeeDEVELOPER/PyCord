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
    contentLength = "Content-Length: " + str(postData)

    b_obj = BytesIO()
    crl = pycurl.Curl()

    if (crl):
        crl.setopt(crl.CAINFO, certifi.where())
        crl.setopt(crl.POST, 1)
        crl.setopt(crl.URL, url)
        crl.setopt(crl.USERAGENT, "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
        headerList = {}
        headerList = crl.setopt_string(headerList, "Accept: */*")
        headerList = crl.setopt_string(headerList, "Content-type: application/json")
        headerList = crl.setopt_string(headerList, authHead)
        headerList = crl.setopt_string(headerList, "Host: discordapp.com")
        contentLength = "Content-Length: " + str(postData)
        headerList = crl.setopt_string(headerList, contentLength)
        crl.setopt(crl.HEADERFUNCTION, debug.display_header)
        crl.setopt(crl.WRITEDATA, b_obj)
        crl.perform()
        crl.close()
        debug.log(debug.headers)
        


    r = requests.get(url)

    debug.log("post data: " + str(postData))
    debug.log("status code: " + str(r.status_code))

    return r.status_code


    