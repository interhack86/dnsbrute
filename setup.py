# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
	name='dnsbrute',
	description='Simple DNS Brute using a dictionary',
	url='https://github.com/interhack86/',
	version='1.0.0',
	author='Kevin Gonzalvo',
	author_email='interhack@gmail.com',
	packages=find_packages(),
	package_data={
	},
	install_requires=[
		'requests',
		'dnspython'
    ]
)
