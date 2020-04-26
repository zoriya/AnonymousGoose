from trick import Trick
from tricks.data.scenario_resource import intro_text
from tricks.data.scenario_resource import event1_text
from term_utils import Term
import time


class Scenario(Trick):
	id_scenario = 1
	nb_of_scenario = 2
	
	@staticmethod
	def intro():
		intro_terminal = Term()
		intro_terminal.print_creepy(intro_text)
		time.sleep(2)

	@staticmethod
	def event1():
		Term()
		Term.print_all(event1_text)
		time.sleep(2)
	
	@property
	def name(self):
		return "Scenario"

	@property
	def delay(self):
		return 5

	@property
	def is_reversible(self):
		return False

	def revert(self):
		pass

	def run(self):
		if not Scenario.id_scenario == -1:
			if Scenario.id_scenario == 1:
				Scenario.intro()
			if Scenario.id_scenario == 2:
				Scenario.event1()
			Scenario.id_scenario += 1
			if Scenario.id_scenario > Scenario.nb_of_scenario:
				Scenario.id = -1


