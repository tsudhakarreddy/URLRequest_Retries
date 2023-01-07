from datetime import datetime, timedelta
import json
import os
import sys
import traceback
import re
import ssl

###For downloading files
import requests
import shutil
import urllib.request
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

retry_strategy = Retry(
    total=3,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 504]
)


def responseCheck(url):
    try:
        adapter = HTTPAdapter(max_retries=retry_strategy)
        http = requests.Session()
        http.mount("https://", adapter)
        http.mount("http://", adapter)
        #resp = http.get(url,verify=False)
        urllink = urllib.request.urlopen(url) 
       
        return [urllink]
    except Exception as e:
           print (e)

def processJson():
    
    link = 'https://leidata-preview.gleif.org/api/v2/golden-copies/publishes?page=1&per_page=1'
    #mf = urllib.request.urlopen(link) 
    resp = responseCheck(link)
    mf = resp[0]
    myfile = mf.readline()
    myfile = myfile.decode('utf-8')
    url = myfile[0:1000]
    Part1 = url.index('"url"') +7
    Part2 = url.index('zip') +3
    url = myfile[Part1:Part2]
    url = url.replace('\\','')

    #print(mf.status)
    print(url)
    

processJson()







