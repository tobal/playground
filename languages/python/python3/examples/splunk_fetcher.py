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

while True:
    search_results = requests.get(baseurl + '/services/search/jobs/' + search_id + '/results/',
                                   auth=(username, password),
                                   verify=False,
                                   data={'output_mode': 'json'})
    if search_results.status_code == 200:
        print(search_results.text)
        break
