#!/usr/bin/env python3


import requests
from sys import argv
from xml.dom import minidom
import urllib3


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
if len(argv) < 4:
    print('Please specify the base url, username and password')
    exit(1)

baseurl, username, password = argv[1], argv[2], argv[3]

baseurl = 'https://10.170.30.100:8089'
username = 'admin'
password = 'TitkoS12'


def get_search_query():
    search_query = 'host="zion" index="local_var_log" process="sshd"'
    if not (search_query.startswith('search') or search_query.startswith("|")):
        search_query = 'search ' + search_query
    return search_query


server_content = requests.post(baseurl + '/services/search/jobs',
                               auth=(username, password),
                               verify=False,
                               data={'search': get_search_query()})
search_id = minidom.parseString(server_content.text).getElementsByTagName('sid')[0].firstChild.nodeValue

print(search_id)
