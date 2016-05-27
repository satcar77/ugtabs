#!/usr/bin/env python

from distutils.core import setup
import ugtabs

with open("README.md") as file:
	long_description = file.read()

setup(
		name=ugtabs.NAME,
		version=ugtabs.VERSION,
		author=ugtabs.AUTHOR,
		author_email=ugtabs.AUTHOR_EMAIL,
		url=ugtabs.URL,
		install_requires=["bs4","lxml"],
		py_modules=["ugtabs"],
		scripts=["ugtabs"],

		)
