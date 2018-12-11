#!/usr/bin/python -u

import urllib
import httplib2
from xml.dom import minidom

baseurl = 'https://localhost:8089'
userName = 'admin'
password = 'password'

searchQuery = '| inputcsv foo.csv | where sourcetype=access_common | head 5'

# Authenticate with server.
# Disable SSL cert validation. Splunk certs are self-signed.
serverContent = httplib2.Http(disable_ssl_certificate_validation=True).request(baseurl + '/services/auth/login',
    'POST', headers={}, body=urllib.urlencode({'username':userName, 'password':password}))[1]

sessionKey = minidom.parseString(serverContent).getElementsByTagName('sessionKey')[0].childNodes[0].nodeValue

# Remove leading and trailing whitespace from the search
searchQuery = searchQuery.strip()

# If the query doesn't already start with the 'search' operator or another 
# generating command (e.g. "| inputcsv"), then prepend "search " to it.
if not (searchQuery.startswith('search') or searchQuery.startswith("|")):
    searchQuery = 'search ' + searchQuery

print searchQuery

# Run the search.
# Again, disable SSL cert validation. 
print httplib2.Http(disable_ssl_certificate_validation=True).request(baseurl + '/services/search/jobs','POST',
    headers={'Authorization': 'Splunk %s' % sessionKey},body=urllib.urlencode({'search': searchQuery}))[1]
