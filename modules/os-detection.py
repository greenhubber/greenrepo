import platform

def run(**args):
	print "[*] In os-detection module."
	info = (platform.machine()+" "+platform.version()+" "+platform.platform()+" "+platform.uname()+" "+platform.processor())
	return info
