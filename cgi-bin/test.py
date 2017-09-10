#!/usr/bin/python

import io
import time
import picamera

my_stream = io.BytesIO()
with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.start_preview()
    # Camera warm-up time
    time.sleep(2)
#    camera.capture('/home/pi/nas/DCIM/foo.jpg')
    camera.capture(my_stream, 'jpeg')

#print "Content-type: text/html"
#print
#print "<html>"
#print "<head>"
#print "<title>test</title>"
#print "</head>"
#print "<body>This page is test page.</body>"
#print "</html>"

print "Content-type: image/jpeg"
print
print my_stream.getvalue()
