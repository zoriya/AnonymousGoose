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
	def get_random_trick(keep_x):
		from tricks.laughing_goose import LaughingGooseTrick
		from tricks.glorify_goose import GlorifyGooseTrick
		from tricks.anim_ascii import AnimAsciiTrick
		from tricks.reflection import ReflectionTrick
		from tricks.rotation import RotationTrick
		from tricks.random_message import RandomMessage
		from tricks.otis_notification import Otis
		
		tricks = [
			GlorifyGooseTrick,
			AnimAsciiTrick,
			LaughingGooseTrick,
			RandomMessage,
			Otis
		]
		x_tricks = [
			ReflectionTrick,
			RotationTrick,
			RandomMessage
		]
		
		if keep_x:
			return random.choice(tricks + x_tricks)()
		return random.choice(tricks)()
