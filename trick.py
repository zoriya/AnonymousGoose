import random
from abc import ABC, abstractmethod


class Trick(ABC):
	@property
	@abstractmethod
	def name(self):
		raise NotImplementedError
	
	@property
	@abstractmethod
	def delay(self):
		return 1
	
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
