import os
from os.path import expanduser,join

def directory(path):
	Total = {}
	path = expanduser(path)
	for (dirname,subdir,subfile) in os.walk(path):
		Total[dirname] = subdir
		for f in subfile:
			subdir.append(f)
	print("The list of file names are",list(Total.values()))
	return Total

print(directory("/home"))
