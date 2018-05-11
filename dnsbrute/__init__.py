#!/usr/bin/python

import sys, string, socket, urllib2, re, dns.resolver

class dnsbrute(object):
	def __init__(self, domain, verbose, output=''):

		self.domain = domain
		self.verbose = verbose
		self.output = open(output, 'w')	if output != '' else ''
		self.outputFlag = True if output != '' else False 
		self.subdomains = []

	def dig_information(self, iterations = 4):
		checks = ['MX', 'NS']
		try:
			for check in checks:
				con = 1
				while iterations >= con:
					for x in dns.resolver.query(self.domain, check):
						try:
							x = str(x)
							if check == 'MX':
								y = x.split(' ')[1].split('.')[0]
							else:
								y = x.split('.')[0]
							info_sub = self.info_subdomain(y)
							if info_sub not in self.subdomains:
								if self.verbose == 'full':
									print ' [*]' + y + ', ' + info_sub 
								if self.outputFlag:
									self.output.write(y + ', ' + info_sub + '\n')
								
								self.subdomains.append(info_sub)
						except:
							pass
					con+=1
		except:
			pass

	def clean_subdomains_dorks(self, info):
		for x in info:
			if re.search(self.domain, x, flags=re.IGNORECASE):
				try:
					info_sub = self.info_subdomain(x.split('.')[0].split('//')[1])
					if info_sub not in self.subdomains:
						if self.verbose == 'full':
							print ' [*]' + x.split('.')[0].split('//')[1]+ ', ' + info_sub 
						if self.outputFlag:
							self.output.write(x.split('.')[0].split('//')[1] + ', ' + info_sub + '\n')
						self.subdomains.append(info_sub)
				except:
					pass
	def dorks(self):
		url = ''.join(("http://www.bing.com/search?q=domain%3a", self.domain))
		request = urllib2.Request(url)
		request.add_header('User-agent','Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:19.0) Gecko/20100101 Firefox/19.0')
		response = urllib2.urlopen(request).read()
		domains_dorks = set(re.findall(r'<h2><a * href="(.+?)"', response))
		self.clean_subdomains_dorks(domains_dorks)

	def info_subdomain(self, line):
		s = socket.gethostbyname_ex(line+"."+self.domain)
		return s[0] + ', ' + s[2][0]

	def brute(self, search_list):

		file = open(search_list,'r'); cnames = open(search_list, 'r').readlines()
		sys.stdout.write("[*]-Using dictionary: " + search_list + " (Loaded " + str(len(cnames)) + " words)\n") if self.verbose == 'full' else ''
		l=0; i=0
		for line in file.read().split('\n'):
			l+=1
			ESC = chr(27)
			sys.stdout.write(ESC + '[2K'+ ESC + '[G') if self.verbose == 'full' else ''
			sys.stdout.write(' [*]' + line+ ', ') if self.verbose == 'full' else ''
			sys.stdout.flush()
			try:
				info = self.info_subdomain(line)
				if self.verbose == 'full':
					if info not in self.subdomains:
						print info
				if self.outputFlag:
					if info not in self.subdomains:
						self.output.write(line + ', ' + info + '\n')
				if info not in self.subdomains:
					self.subdomains.append(info)
				i+=1
			except:
				pass
		sys.stdout.write(ESC + '[2K'+ESC + '[G') if self.verbose == 'full' else ''
		sys.stdout.write("[*]-Total assets found: " + str(i)) if self.verbose == 'full' else ''
		return self.subdomains
