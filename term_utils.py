import os
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
		CommandHelper.run(f"{Term.find_terminal()} &")
		return f"/dev/pts/{min(list)}"

	@staticmethod
	def find_terminal():
		if Term.terminal:
			return Term.terminal
		for term in Term.terminal_list:
			if not CommandHelper.run(f"{term} &"):
				Term.terminal = term
				return term
