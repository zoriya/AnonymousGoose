import time
import os
import random

from trick import Trick


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
		selected = random.choice(["x", "y", "xy"])
		os.system(f"xrandr --output $(xrandr -q | grep ' connected' | cut -f 1 -d ' ' | cut -f 1 -d '\n') --reflect {selected}")
		time.sleep(5)
		os.system("xrandr --output $(xrandr -q | grep ' connected' | cut -f 1 -d ' ' | cut -f 1 -d '\n') --reflect normal")
