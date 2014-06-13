import urllib2

req = urllib2.Request('http://facebook.com/ahsa17')
response = urllib2.urlopen(req)
the_page = response.read()

print the_page
