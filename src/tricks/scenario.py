from trick import Trick
from tricks.data.scenario_resource import event
from term_utils import Term
import time


class Scenario(Trick):
	id_scenario = 0

	@staticmethod
	def event(text_event):
		intro_terminal = Term()
		intro_terminal.print_creepy(text_event)
		time.sleep(2)
	
	@property
	def name(self):
		return "Scenario"

	@property
	def delay(self):
		if Scenario.id_scenario < len(event):
			return 5
		return 0

	@property
	def is_reversible(self):
		return False

	def revert(self):
		pass

	def run(self):
		if Scenario.id_scenario < len(event):
			Scenario.event(event[Scenario.id_scenario])
			Scenario.id_scenario += 1


