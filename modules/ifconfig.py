import os
import subprocess

def run(**args):
	print "[*] in ifconfig module"
	output = popen(["ifconfig"], stdout=PIPE).communicate()[0]
	return output
