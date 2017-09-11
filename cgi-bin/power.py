#!/usr/bin/python

import os
print "Content-type: text/html";
print
print "reboot"
#print "<font size=+1>Environment</font><\br>";
#for param in os.environ.keys():
#    print "<b>%20s</b>: %s<\br>" % (param, os.environ[param])
os.system("sudo shutdown -r now")