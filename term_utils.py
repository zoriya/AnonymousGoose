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
		"final-term",
		"finalTerm",
		"terminology",
		"xfce4-terminal",
		"xterm",
		"lilyterm",
		"sakura",
		"rxvt-unicode"
	]
	
	def __init__(self):
		self.tty = self.create_tty()

	def print(self, msg):
		try:
			with open(self.tty, "w") as file:
				file.write(msg)
				return True
		except PermissionError:
			return False
		except OSError:
			return False

	def print_creepy(self, msg):
		try:
			with open(self.tty, "w") as file:
				for char in msg:
					try:
						file.write(char)
						file.flush()
						time.sleep(random.uniform(0, 0.2))
					except KeyboardInterrupt:
						pass
		except PermissionError:
			return False
		except OSError:
			return False

	@staticmethod
	def print_all_creepy(msg):
		f = []
		for file in os.listdir("/dev/pts"):
			if file.isdigit():
				try:
					f.append(open(f"/dev/pts/{file}", "w"))
				except PermissionError:
					pass
				except OSError:
					pass

		for char in msg:
			for fd in f:
				fd.flush()
				fd.write(char)
			time.sleep(random.uniform(0, 0.2))

		for file in f:
			file.close()

	@staticmethod
	def print_all(msg):
		for file in os.listdir("/dev/pts"):
			if file.isdigit():
				try:
					with open(f"/dev/pts/{file}", "w") as f:
						f.write(msg)
				except PermissionError:
					pass
				except OSError:
					pass

	@staticmethod
	def create_tty():
		li = []
		current = None
		for tty in os.listdir("/dev/pts"):
			if tty.isdigit():
				li.append(int(tty))
		CommandHelper.run_async(Term.find_terminal())
		time.sleep(1)
		for tty in os.listdir("/dev/pts"):
			if tty.isdigit():
				if int(tty) not in li:
					current = int(tty)
		return f"/dev/pts/{current}"

	@staticmethod
	def find_terminal():
		if Term.terminal:
			return Term.terminal
		for term in Term.terminal_list:
			if shutil.which(term) is not None:
				Term.terminal = term
				return term
