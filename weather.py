# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 14:52:52 2019

@author: saras
"""

import requests


endpoint = "http://api.openweathermap.org/data/2.5/weather"


payload = {"q": "London,UK", "units":"metric", "appid":"379d652027e0c8240aeb2dbd516bdff0"}


response = requests.get(endpoint, params=payload)
data = response.json()

print (data)
print ('this is what data looks like \n')
print (response.url)
print (response.status_code)
print (response.headers["content-type"])