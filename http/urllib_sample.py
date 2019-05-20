import urllib.request

req = urllib.request.Request('http://www.google.com')

with urllib.request.urlopen(req) as response:
   the_page = response.read()