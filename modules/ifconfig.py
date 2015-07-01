import os
import subprocess

def run(**args):
	output = popen(["ifconfig"], stdout=PIPE).communicate()[0]
	return str(output)
