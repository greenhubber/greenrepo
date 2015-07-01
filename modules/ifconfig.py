import os

def run(**args):
	print "[*] in ifconfig module"
	handle = os.popen("ifconfig")
    	line = " "
	output = "ifconfig: "
    	while line:
        	line = handle.read()
        	print line
		output = (output + line)
    	handle.close()
	return output
