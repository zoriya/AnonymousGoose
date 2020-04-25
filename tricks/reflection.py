import time
import os

from trick import Trick
from command_helper import CommandHelper


class ReflectionTrick(Trick):
	@property
	def name(self):
		return "Reflection"

	@property
	def delay(self):
		return 5

	@property
	def is_reversible(self):
		return False

	def revert(self):
		pass

	def run(self):
		os.system("xrandr --output $(xrandr -q | grep ' connected' | cut -f 1 -d ' ' | cut -f 1 -d '\n') --reflect x")
		time.sleep(5)
		os.system("xrandr --output $(xrandr -q | grep ' connected' | cut -f 1 -d ' ' | cut -f 1 -d '\n') --reflect normal")
