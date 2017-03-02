#!/usr/bin/env python

import os
import sys

sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

home_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(home_dir)

print "Script file directory: %s" % home_dir
log_list = []

for root, dirs, files in os.walk(home_dir):
	    for f in files:
	        if f.endswith('.py'):
	             log_list.append(os.path.join(root, f))

if not log_list:
	sys.exit("No files detected")

print "Python files detected:"
for x in list(enumerate(log_list)):
	if 'CRFix.py' in x[1]:
		continue
	print "    ", 
	print (x[0], "/".join(x[1].strip("/").split('/')[1:]))
print ""

filename = log_list[int(raw_input('Enter file index: '))]

with open(filename, 'rb+') as f:
    content = f.read()
    f.seek(0)
    f.write(content.replace(b'\r', b''))
    f.truncate()

print 'CR characters successfully removed from %s' % filename