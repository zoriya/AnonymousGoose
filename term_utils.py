import os
import shutil
import time
import random
from command_helper import CommandHelper


class Term:
	terminal = ""

	terminal_list = [
		"konsole",
		"terminator",
		"tilda",
		"guake",
		"yakuake",
		"roxterm",
		"eterm",
		"Rxvt",
		"wterm",
		"lxterminal",
		"termKit",
		"st",
		"gnome-terminal",
		"final_term",
		"finalTerm",
		"terminology",
		"xfce4_terminal",
		"xterm",
		"lilyterm",
		"sakura",
		"rxvt-unicode"
	]

	def __init__(self):
		self.tty = self.create_tty()
		time.sleep(1)

	def print(self, msg):
		with open(self.tty, "w") as file:
			file.write(msg)

	def print_creepy(self, msg):
		with open(self.tty, "w") as file:
			for char in msg:
				file.write(char)
				file.flush()
				time.sleep(random.uniform(0, 0.2))

	@staticmethod
	def print_all_creepy(msg):
		f = []
		for file in os.listdir("/dev/pts"):
			if file.isdigit():
				f.append(open(f"/dev/pts/{file}", "w"))
		for char in msg:
			for fd in f:
				fd.flush()
				fd.write(char)
		time.sleep(random.uniform(0, 0.2))

	@staticmethod
	def print_all(msg):
		for file in os.listdir("/dev/pts"):
			if file.isdigit():
				f = open(f"/dev/pts/{file}", "w")
				f.write(msg)

	@staticmethod
	def create_tty():
		list = [i for i in range(100)]
		for tty in sorted(os.listdir("/dev/pts")):
			if tty.isdigit():
				if int(tty) in list:
					list.remove(int(tty))
		CommandHelper.run_async(Term.find_terminal())
		return f"/dev/pts/{min(list)}"

	@staticmethod
	def find_terminal():
		if Term.terminal:
			return Term.terminal
		for term in Term.terminal_list:
			if shutil.which(term) is not None:
				Term.terminal = term
				return term

