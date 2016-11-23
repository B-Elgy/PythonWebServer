#Import Statements
import datetime
import sys
import os
import socket as sock
import PythonLibraries.optHandler as optHandler
import PythonLibraries.returnGenerators as returnGens

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
        forever = False
        try:
            numOfReq=int(scanner.opts["-r"])
            if(numOfReq == 0):
                forever = True
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
    for loopIter in range(numOfReq) or forever:
        print("Waiting For Connection")
        con, add = s.accept()
        print("Accepted Connection At " + str(add) + ".")
        rec = con.recv(2048)
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

