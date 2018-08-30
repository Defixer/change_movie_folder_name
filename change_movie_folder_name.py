import os
import sys

files = os.listdir(sys.argv[1])
for file in files:
	new_file = os.path.join(sys.argv[1], file.split("[")[0])
	old_file = os.path.join(sys.argv[1], file)
	os.rename(old_file, new_file)