#Args:Host, Port, Number of Requests To Be Filled, Backlog
#Import Statements
import datetime
import sys
import os
import socket as sock
import PythonLibraries.optHandler as optHandler
endl="\n"
def genHeader(f):
    h=[]
    if(not os.path.exists("./" + f)):
        f="404Error.html"
        h.append(("HTTP/1.1 404 Not Found"+endl).encode())
    else:
        h.append(("HTTP/1.1 200 OK"+endl).encode())
    dateH=datetime.datetime.now().strftime("Date: %a, %d %b %Y %H:%M:%S EST"+endl).encode()
    h.append(dateH)
    fobj=open("./"+f)
    conLen=len(fobj.read())
    fobj.seek(0)
    conLenH=("Content-Length: " + str(conLen) + endl).encode()
    h.append(conLenH)
    conTypeH=("Content-Type: text/html" + endl).encode()
    h.append(conTypeH)
    return h

def genReturn(f):
    ha=genHeader(f)
    if(not os.path.exists("./"+f)):
        f="404Error.html"
    h=""
    for hl in ha:
        h=h+hl.decode()
    h=h.encode()
    bendl=endl.encode()
    r=h+bendl
    fc=""
    fa=open("./"+f).readlines()
    for fl in fa:
        fc=fc+fl
    fc=fc.encode()
    r=r+fc
    return r

def main(a):
    #Argument Handling
    scanner=optHandler.OptScanner(flagsNeedArgs=False)
    scanner.scan(a)
    #Help
    if("-H" in scanner.flags):
        print("Python Server Host\n\nSettings:\n\t-h: Host\n\t-p: Port\n\t-b: Backlog\n\t-r: Number Of Requests To Be Filled")
        sys.exit()

    #Host
    if("-h" in scanner.flags):
        host=scanner.opts["-h"]
    else:
        host=sock.gethostname()

    #Port
    if("-p" in scanner.flags):
        try:
            port=int(scanner.opts["-p"])
        except ValueError:
            print("Port Must Be An Integer")
    else:
        port=8080

    #Backlog
    if("-b" in scanner.flags):
        try:
            backlog=int(scanner.opts["-b"])
        except ValueError:
            print("Backlog Must Be An Integer")
    else:
        backlog=3

    #Number Of Requests To Be Filled
    if("-r" in scanner.flags):
        try:
            numOfReq=int(scanner.opts["-r"])
        except ValueError:
            print("Number Of Requests Must Be An Integer")
    else:
        numOfReq=5

    #More Setup
    endl="\n"
    sAdd=(host,port)
    s=sock.socket()
    s.bind(sAdd)
    s.listen(backlog)
    print("Server Starting. Listening At " + str(host) + ":" + str(port) +
          " With A Backlog For " + str(backlog) + " Clients. Responding to " +
          str(numOfReq) + " requests.")
    #Main Loop
    for loopIter in range(numOfReq):
        print("Waiting For Connection")
        con, add = s.accept()
        print("Accepted Connection At " + str(add) + ".")
        rec = con.recv(512)
        rec = rec.decode()
        print(rec)
        page=""
        l=5
        while(rec[l]!=" "):
            page=page+rec[l]
            l=l+1
        if(page==""):
            page="index.html"
        print(page)
        con.send(genReturn(page))
        print(rec)
        con.close()
        c=False
    s.close()
    print("Server Closed")
if __name__ == '__main__':
        main(sys.argv[1:])

