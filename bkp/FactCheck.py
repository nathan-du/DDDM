#!/usr/bin/python3.4

import sys
from findTable import findTable as ft

if len(sys.argv) < 2:
	print("Please provide a statement to be checked")
	exit(1)

result = ft(sys.argv[1])
print(str(result["truth"]))
print(str(result["reason"]))
