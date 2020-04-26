from data.scenario_resource import random_text
from term_utils import Term
from trick import Trick
import random

class RandomMessage(Trick):
    @property
    def name(self):
        return "RandomMessage"

    @property
    def delay(self):
        return 5

    @property
    def is_reversible(self):
        return False

    def revert(self):
        pass

    def run(self):
        randtext_term = Term()
        randtext_term.print_creepy(random.choice(random_text))
