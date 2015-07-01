import os

def run(**args):
	print "[*] in ifconfig module"
	output = os.popen(["ifconfig"], stdout=PIPE).communicate()[0]
	return output
