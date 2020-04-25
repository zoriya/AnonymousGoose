#!/usr/bin/env python3
import time
import pyxhook

from term_utils import Term
from command_helper import CommandHelper


class AnonymousGoose:
	def __init__(self):
		self.should_exit = False
		self.stopped = False
		self.tricks = []
		self.keyboard_listener = pyxhook.HookManager()
		self.keyboard_listener.KeyUp = self.key_pressed
		self.keyboard_listener.HookKeyboard()
		self.keyboard_listener.start()
		# print(DetectTerm.find_terminal())
		# time.sleep(1)
		Term.print_all("YOU HAVE BEEN HACKED.\n")

	def __del__(self):
		if not self.stopped:
			self.keyboard_listener.cancel()

	def run(self):
		while not self.should_exit:
			try:
				if CommandHelper.run("killall htop") == 0 or CommandHelper.run("killall top") == 0:
					Term.print_all("You tough that this will be as easy as this?\n")
				time.sleep(1)
			except KeyboardInterrupt:
				...

	def key_pressed(self, key):
		if key.Ascii == 27:
			self.should_exit = True

	def stop(self):
		if self.stopped:
			return
		self.keyboard_listener.cancel()
		self.stopped = True


if __name__ == "__main__":
	goose = AnonymousGoose()
	term = Term()
	print(term.tty)
	goose.run()
	goose.stop()
