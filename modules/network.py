import urllib
import re

def run(**args):
	print "[*] In network module."
	url = "http://checkip.dyndns.org"
	request = urllib.urlopen(url).read()
	theIP = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}", request)
	return str(theIP)
