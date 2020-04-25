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

	@property
	@abstractmethod
	def is_reversible(self):
		raise NotImplementedError
	
	@abstractmethod
	def revert(self):
		raise NotImplementedError
	
	@abstractmethod
	def run(self):
		raise NotImplementedError
	
	@staticmethod
	def get_random_trick():
		from Tricks.laughing_goose import LaughingGooseTrick
		from Tricks.anim_ascii import AnimAsciiTrick
		tricks = [
			LaughingGooseTrick,
			AnimAsciiTrick
		]

		return random.choice(tricks)()
