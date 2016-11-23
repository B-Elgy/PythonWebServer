#Import Statements
import datetime
import os
import re

#Variable Definitions
endl = "\n"
bendl = endl.encode()
#Content Type Returns
contentTypes = {"html":"text/html", "js":"application/javascript", "json":"application/json", "txt":"text/plain", "jpg":"image/jpeg", "jpeg":"image/jpeg", "png":"image/png", "css":"text/css"}
#Function Definitions
#Main Functions
#Header Function
def genHeaders(f):
    #Local Functions and Variable
    headers = ""
    encodedHeaders = b""
    def headerAppend(header):
        headers = headers + header
    #Headers Creation
    #Status Header  
    if(f == "404Error.html"): #404 Not Found Status Header
        statusHeader = "HTTP/1.1 404 Not Found" + endl
    else: #200 OK Status Header
        statusHeader = "HTTP/1.1 200 OK" + endl
    headerAppend(statusHeader)
    #Date Header
    dateHeader = datetime.datetime.now().strftime("Date: %a, %d %b %Y %H:%M:%S EST"+endl)
    headerAppend(dateHeader)
    #Content-Type Header
    contentTypeHeader = "Content-Type: " + contentTypes[re.split("\.",f)[1]] + endl
    headerAppend(contentTypeHeader)
    #Content-Length Header
    contentLengthHeader = "Content-Length: " + len(open("./html/" + f, "rb").read()) + endl
    headerAppend(contentLengthHeader)
    headerAppend(endl)
    return (headers,headers.encode())

#Return Function
def genReturn(f):
    if(not os.path.exists("./html/" + f)): #If Page Doesn't Exist
        f = "404Error.html"
    headers, encodedHeaders = genHeaders(f)
    returnResponse = encodedHeaders + open("./html/" + f, "rb").read()
    return returnResponse
