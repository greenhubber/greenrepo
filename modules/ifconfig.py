import os
import subprocess

def run(**args):
	output = Popen(["ifconfig"], stdout=PIPE).communicate()[0]
	return str(output)
