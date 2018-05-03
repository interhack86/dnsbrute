#!/usr/bin/python

import sys, string, socket

def help():
	print "\nUsage: python dnsbrute.py domain_name dictionary\n"
	sys.exit()

if len(sys.argv) < 1 or len(sys.argv) > 3:
	help()
elif len(sys.argv) == 3:
	domain_name =  sys.argv[1]
	filename =  sys.argv[2]
else:
	help()


file = open(filename,'r')
fc = open(filename, 'r')
cnames = fc.readlines()

out = open('results_' + domain_name + '.txt', 'w')

sys.stdout.write("[*]-Using dictionairy: " + filename + " (Loaded " + str(len(cnames)) + " words)\n")
out.write("[*]-Using dictionairy: " + filename + " (Loaded " + str(len(cnames)) + " words)\n")
l=0
i=0
for line in file.read().split('\n'):
	l=l+1
	ESC = chr(27)
	sys.stdout.write(ESC + '[2K'+ ESC + '[G')
	sys.stdout.write(' [*]' + line+ ', ')
	sys.stdout.flush()
	try:
		s = socket.gethostbyname_ex(line+"."+domain_name)
		print s[0] + ', ' + s[2][0]
		out.write(' [*]' + line+ ', ' + s[0] + ', ' + s[2][0] + '\n')
		i=i+1
	except:
		pass
sys.stdout.write(ESC + '[2K'+ESC + '[G')
sys.stdout.write("[*]-Total assets found:", i)
file.close()
fc.close()
out.close()