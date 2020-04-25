import time
import os

from trick import Trick


class RotationTrick(Trick):
	@property
	def name(self):
		return "Rotation"

	@property
	def delay(self):
		return 5

	@property
	def is_reversible(self):
		return False

	def revert(self):
		pass

	def run(self):
		os.system("xrandr --output $(xrandr -q | grep ' connected' | cut -f 1 -d ' ' | cut -f 1 -d '\n') --rotation inverted")
		time.sleep(5)
		os.system("xrandr --output $(xrandr -q | grep ' connected' | cut -f 1 -d ' ' | cut -f 1 -d '\n') --rotation normal")
