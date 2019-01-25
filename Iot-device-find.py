"""
This script retrieves an authentication token from DNAC to be used for the API Find Device
Mark Ellwanger - modified from @aradford123
"""

import requests   # We use Python "requests" module to do HTTP GET query
from requests.auth import HTTPBasicAuth  #DNAC uses basic Authentication to get a token
import json       # Import JSON encoder and decode module

requests.packages.urllib3.disable_warnings() # Disable warnings

# DNAC IP, modify these parameters if you are using your own DNAC
dnac_ip = "sandboxdnac.cisco.com"
username = "devnetuser"
password = "Cisco123!"
version = "v1"


# POST token API URL
post_url = "https://" + dnac_ip + "/api/system/" + version + "/auth/token"

# All DNAC REST API request and response content type is JSON.
headers = {'content-type': 'application/json'}

# Make request and get response - "resp" is the response of this request
resp = requests.post(post_url, auth=HTTPBasicAuth(username=username,password=password), headers=headers,verify=False)
print ("Request Status: ",resp.status_code)

def get_host(ip=None, mac=None):
     if ip is not None:
          url = "host?hostIp=%s" % ip
     elif mac is not None:
          url = "host?hostMac=%s" % mac
      return get_url(url)

 def get_wlc(id):
      return get_url("network-device/%s" % id)
