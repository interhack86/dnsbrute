# dnsbrute:
Simple DNS Brute using a dictionary

# Usage:
python -m dnsbrute -h

usage: -m dnsbrute [-h] [-d DOMAIN] [-e ENGINE] -w WORDLIST [-o OUTPUT]
                   [-v VERBOSE]

DNS bruteforce

optional arguments:
  -h, --help   show this help message and exit
  -d DOMAIN    domain
  -e ENGINE    Search domains using dorks [y/n]
  -w WORDLIST  Wordlist to use in bruteforce
  -o OUTPUT    write results in file
  -v VERBOSE   Verbosity none/full

# Usage docker with default dictionaries:
docker run -it interhack/dnsbrute -d <domain> -w <wordlist>

## Defaults Wordlists in docker:

- bitquark-subdomains-top100K.txt
- deepmagic.com-top500prefixes.txt
- deepmagic.com-top50kprefixes.txt
- fierce-hostlist.txt
- namelist.txt 
- sortedcombied-knock-dnsrecon-fierce-reconng.txt
- subdomains-top1mil-110000.txt
- subdomains-top1mil-20000.txt
- subdomains-top1mil-5000.txt

# Usage docker with others dictionaries:
docker run -it -v path_dictionaries:/domains/ interhack/dnsbrute -d <domain> -w <wordlist>