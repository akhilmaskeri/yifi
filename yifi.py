import requests
from urlGenrator import urlGenrator
import json,sys

url = urlGenrator()
url = url.genrate(sys.argv)

print url

