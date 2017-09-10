#!/usr/bin/python

import os
import urllib
import urlparse
import io
import picamera

q_str = os.environ.get("QUERY_STRING", "")
q = urlparse.parse_qs(q_str)

my_stream = io.BytesIO()
with picamera.PiCamera() as camera:
    camera.resolution = (int(q["w"][0]),int(q["h"][0]))
    #camera.start_preview()
    # Camera warm-up time
    #time.sleep(2)
#    camera.capture('/home/pi/nas/DCIM/foo.jpg')
    camera.capture(my_stream, 'jpeg')

#print "Content-type: text/html";
#print
#print "<font size=+1>Environment</font><\br>";
#for param in os.environ.keys():
#    print "<b>%20s</b>: %s<\br>" % (param, os.environ[param])
print "Content-type: image/jpeg"
print
print my_stream.getvalue()
