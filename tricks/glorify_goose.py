import os
import random

from command_helper import CommandHelper
from trick import Trick


class GlorifyGooseTrick(Trick):
	@property
	def name(self):
		return "Glorify goose"

	@property
	def delay(self):
		return 5

	@property
	def is_reversible(self):
		return False

	def revert(self):
		pass

	def run(self):
		images = os.listdir("data/glorify")
		CommandHelper.run_async(f"xdg-open data/glorify/{random.choice(images)}")
