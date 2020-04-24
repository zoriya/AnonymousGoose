import os


def my_print(msg):
	for file in os.listdir("/dev/pts"):
		if file.isdigit():
			f = open(f"/dev/pts/{file}", "w")
			f.write(msg)
