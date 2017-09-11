#!/usr/bin/python

import os
import urllib
import urlparse

q_str = os.environ.get("QUERY_STRING", "")
q = urlparse.parse_qs(q_str)
command = "sudo shutdown -h now"
if q["mode"]:
	if q["mode"][0] == "reboot":
		command = "sudo reboot"

print "Content-type: text/html";
print
print "reboot"
#print "<font size=+1>Environment</font><\br>";
#for param in os.environ.keys():
#    print "<b>%20s</b>: %s<\br>" % (param, os.environ[param])
os.system(command)