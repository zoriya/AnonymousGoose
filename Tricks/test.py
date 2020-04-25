from trick import Trick


class TestTrick(Trick):
	@property
	def name(self):
		return "Test"
	
	@property
	def delay(self):
		return 1
	
	def run(self):
		print("Test succeed")
