import os
import sys

files = os.listdir(sys.argv[1])
for file in files:
	if file[0] != ".":
		if "YTS" in file:
			print("File: {}".format(file))
			old_file = os.path.join(sys.argv[1], file)
			print("Old File: {}".format(old_file))
			new_file = os.path.join(sys.argv[1], file.split("[")[0].rstrip())
			print("New File: {}".format(new_file))
			os.rename(old_file, new_file)