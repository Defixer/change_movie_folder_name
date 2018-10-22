import os
import sys
import tkinter as tk
from tkinter import filedialog

application_window = tk.Tk()
directory = filedialog.askdirectory(parent=application_window,
										initialdir=os.getcwd(),
										title="Please select a folder")
files = os.listdir(directory)
for file in files:
	if file[0] != ".":
		if "YTS" in file:
			print("File: {}".format(file))
			old_file = os.path.join(directory, file)
			print("Old File: {}".format(old_file))
			new_file = os.path.join(directory, file.split("[")[0].rstrip())
			print("New File: {}".format(new_file))
			os.rename(old_file, new_file)