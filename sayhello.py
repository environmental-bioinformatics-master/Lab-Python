#!/user/bin/env python3
"""
sayhello.py name1 [name2] [name3]... etc. 
"""
import sys

if len(sys.argv) < 2:
	print("Please specify at least one name...")

elif len(sys.argv) == 2:
	print("Hello", sys.argv[1])
elif len(sys.argv) == 3: 
	print("Hello", sys.argv[1], "and", sys.argv[2])
else:
	names = sys.argv[1:-1]
	lastname = sys.argv[-1]
	print("Hello", ', '.join(names), 'and', lastname)

