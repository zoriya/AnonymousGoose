#!/usr/bin/env python3
import time
import pyxhook

from term_utils import TermUtils
from detect_term import DetectTerm
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
		TermUtils.print("YOU HAVE BEEN HACKED.\n")
		self.run()

	def __del__(self):
		if not self.stopped:
			self.keyboard_listener.cancel()

	def run(self):
		while not self.should_exit:
			if CommandHelper.run("killall htop") == 0 or CommandHelper.run("killall top") == 0:
				TermUtils.print("You tough that this will be as easy as this?\n")
			time.sleep(1)

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
	goose.stop()
