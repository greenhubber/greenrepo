import os
import subprocess

def run(**args):
	output = Popen(["mycmd", "myarg"], stdout=PIPE).communicate()[0]
	return str(output)
