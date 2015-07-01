import os

def run(**args):
	print "[*] in ifconfig-command module(based on the exec-module)"
	handle = os.popen("ifconfig")
    	line = " "
	output = "ifconfig: "
    	while line:
        	line = handle.read()
		output = (output + line)
    	handle.close()
	return output
