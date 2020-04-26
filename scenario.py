from data.scenario_resource import intro_text
from term_utils import Term
import time

def intro():
    intro_terminal = Term()
    intro_terminal.print_creepy(intro_text)
    time.sleep(2)
