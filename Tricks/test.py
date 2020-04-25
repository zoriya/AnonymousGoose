from trick import Trick


class TestTrick(Trick):
	@property
	def name(self):
		return "Test"
	
	@property
	def delay(self):
		return 1
	
	@property
	def is_reversible(self):
		return False
	
	def revert(self):
		pass
	
	def run(self):
		print("Test succeed")
