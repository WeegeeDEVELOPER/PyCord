import requests
import time
import pycurl
import certifi

from io import BytesIO
from urllib.parse import urlencode
from requests.api import head

from scripts import status
from scripts import debug

resp = 0

def discordPostData(url, postData, authToken):
    authHead = "Authorization: " + str(authToken)
    contentLength = "Content-Length: " + str(postData)

    #b_obj = BytesIO()
    #crl = pycurl.Curl()

    #body = BytesIO()
    #header = BytesIO()

#--
    #if (crl):
        #crl.setopt(crl.CAINFO, certifi.where())
        #crl.setopt(crl.POST, 1)
        #crl.setopt(crl.URL, url)
        #crl.setopt(crl.USERAGENT, "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
        #crl.setopt(crl.WRITEDATA, body)
        #crl.setopt(crl.WRITEDATA, header)
        #crl.setopt(crl.SSL_VERIFYHOST, 0)
        #crl.setopt(crl.SSL_VERIFYPEER, 0)
        #crl.setopt(crl.CONNECTTIMEOUT, 3)
        #crl.setopt(crl.FOLLOWLOCATION, 1)
        #crl.setopt(crl.NOPROGRESS, 1)
        #headerList = pycurl.
        #headerList = crl.setopt(headerList, "Accept: */*")
        #headerList = crl.setopt(headerList, "Content-type: application/json")
        #headerList = crl.setopt(headerList, authHead)
        #headerList = crl.setopt(headerList, "Host: discordapp.com")
        #contentLength = "Content-Length: " + str(postData)
        #headerList = crl.setopt(headerList, contentLength)
        #crl.setopt(crl.HEADERFUNCTION, debug.display_header)
        #crl.setopt(crl.WRITEDATA, b_obj)
        #crl.perform()
        #crl.close()
        #debug.log(debug.headers)
#--

    #if (status.mustDebug):
        #crl.setopt(crl.CAINFO, certifi.where())
        #crl.setopt(crl.URL, url)
        #crl.setopt(crl.HEADERFUNCTION, debug.display_header)
        #crl.setopt(crl.WRITEDATA, b_obj)
        #crl.perform()
        #crl.close()
        #get_body = b_obj.getvalue()
        #debug.log('Output of GET request:\n%s' % get_body.decode('utf8')) 
        


    r = requests.get(url)

    login = requests.post(url, data=postData)

    debug.log("post data: " + str(postData))
    debug.log("status code: " + str(r.status_code))
    debug.log(login)

    resp = r.status_code


    