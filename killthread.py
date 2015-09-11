# python2.7.5
# author : eric zhang
# email  : ericnomail@gmail.com
# twitter: @loveisbug
#    http://weibo.com/loveisbug
# date        version    PIC    comments
# 20150910    0.0.1      eric 
# 20150911    0.0.2      eric   use pgrep.

import os, sys, re

def kill_by_name(name):
	print name
	cmd =  'ps aux|grep %s'%name
	f = os.popen(cmd)
	txt = f.read()
	regex = re.compile(r'\w+\s+(\d+)\s+.*')
	ids = regex.findall(txt)

	cmd = 'kill %s'%' '.join(ids)
	os.system(cmd)

def kill_by_name_pgrep(name):
	print name
	cmd = 'pgrep %s'%name
	txt = os.popen(cmd).read().splitlines()
	cmd = 'kill %s'%' '.join(txt)
	os.system(cmd)
	

if len(sys.argv) > 1:
    print kill_by_name_pgrep(sys.argv[1])
else:
    print "Please input the thread name."