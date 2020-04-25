import random
from abc import ABC, abstractmethod


class Trick(ABC):
	def __init__(self):
		self.name = "Undefined"
		self.delay = 1
	
	@abstractmethod
	def run(self):
		raise NotImplementedError
	
	@staticmethod
	def get_random_trick():
		from Tricks.test import TestTrick
		tricks = [
			TestTrick
		]

		return random.choice(tricks)()
