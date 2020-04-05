#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 10:48:15 2020

@author: jc
"""


import requests

dict_to_send = {"hostname": "fibonacci.com", "ip": "0.0.0.0", "as_ip": "0.0.0.0", "as_port": "53533"}
fs_ip = 'http://0.0.0.0'
fs_port = '9090'
fs_add = fs_ip + ':' + fs_port + '/register'
# print(fs_add)
res = requests.put(fs_add, json=dict_to_send)
print(res.text)


dict_to_send = {'hostname': 'fibonacci.com', 'fs_port': '9090', 'as_ip': '0.0.0.0', 'as_port': '53533', 'number': 9}
us_ip = 'http://0.0.0.0'
us_port = '8080'
us_add = us_ip + ':' + us_port + '/fibonacci'
res = requests.get(us_add, params=dict_to_send)
print(res.text)

dict_to_send = {'hostname': 'fibonacci.com', 'fs_port': '9090', 'as_ip': '0.0.0.0', 'as_port': '53533', 'number': 5}
us_ip = 'http://0.0.0.0'
us_port = '8080'
us_add = us_ip + ':' + us_port + '/fibonacci'
res = requests.get(us_add, params=dict_to_send)
print(res.text)

dict_to_send = {'hostname': 'fibonacci.com', 'fs_port': '9090', 'as_ip': '0.0.0.0', 'as_port': '53533', 'number': 'X'}
us_ip = 'http://0.0.0.0'
us_port = '8080'
us_add = us_ip + ':' + us_port + '/fibonacci'
res = requests.get(us_add, params=dict_to_send)
print(res.text)