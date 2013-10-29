#!/usr/bin/env python

import sys
import json
import argparse

parser = argparse.ArgumentParser(description='Concatenate JSON files that have a list as the root element.')
parser.add_argument('input', action='append', nargs='+',type=file)
parser.add_argument('-o', '--output', action='store',type=argparse.FileType('w'), required=True)
args = parser.parse_args(sys.argv[1:])

contents=[]
def traverse(o, tree_types=(list, tuple)):
	if isinstance(o, tree_types):
		for value in o:
			for subvalue in traverse(value):
				yield subvalue
	else:
		yield o

for input in traverse(args.input):
	content = input.read()
	contents.append(json.loads(content))

outcontents = []
for c in contents:
	outcontents.extend(c)

args.output.write(json.dumps(outcontents));

