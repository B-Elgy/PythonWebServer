#Import Statements
import datetime
import re

#Variable Definitions
endl = "\n"
bendl = endl.encode()
#Content Type Returns
contentTypes = {"html":"text/html", "js":"application/javascript", "json":"application/json", "txt":"text/plain", "jpg":"image/jpeg", "jpeg":"image/jpeg", "png":"image/png", "css":"text/css"}
contentTypeReturnFormats = {"html":"text", "js":"text", "json":"text", "txt", "text", "jpg"}
#Function Definitions
    #Helper Functions
        #Get Content Type Header
def genContentType(f):
    name, ext = tuple(re.split("\." , f))
    contentType = contentTypes[ext]
    
    
#Main Functions
    #Header Function
def genHeaders(f):
    #Local Functions and Variable
    headers = ""
    encodedHeaders = b""
    def headerAppend(header,encodedHeader):
        headers = headers + header
        encodedHeaders = encodedHeaders + encodedHeader
    #Headers Creation
    #Status Header  
    if(f == "404Error.html"): #404 Not Found Status Header
        statusHeader = "HTTP/1.1 404 Not Found" + endl
    else: #200 OK Status Header
        statusHeader = "HTTP/1.1 200 OK" + endl
    encodedStatusHeader = statusHeader.encode()
    headerAppend(statusHeader,encodedStatusHeader)
    #Date Header
    dateHeader = datetime.datetime.now().strftime("Date: %a, %d %b %Y %H:%M:%S EST"+endl)
    encodedDateHeader = dateHeader.encode()
    headerAppend(dateHeader, encodedDateHeader)
    
