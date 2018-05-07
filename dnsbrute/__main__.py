#!/usr/bin/python

import argparse
from dnsbrute import dnsbrute


if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='DNS bruteforce', prog='-m dnsbrute')
	parser.add_argument('-d', action="store", dest="domain", default="google.es", help="domain")
	parser.add_argument('-e', action="store_true", dest="engine", default='n', help="Search domains using dorks")
	parser.add_argument('-w', action="store", dest="wordlist", required=True, help="Wordlist to use in bruteforce")
	parser.add_argument('-o', action="store", dest="output", default='', help="write results in file")
	parser.add_argument('-v', action="store", dest="verbose", default='full', help="Verbosity none/full")

	args = parser.parse_args()
	
	working = dnsbrute(args.domain, args.verbose, args.output)
	if args.engine:
		working.dorks()

	working.brute(args.wordlist)
