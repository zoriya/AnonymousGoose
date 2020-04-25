#!/usr/bin/env python3
import time

from term_utils import Term
from detect_term import DetectTerm
from command_helper import CommandHelper

print(Term.find_terminal())
time.sleep(1)
Term.print_all("YOU HAVE BEEN HACKED.\n")

term1 = Term.create_tty()
print(term1)
term2 = Term.create_tty()
print(term2)
term3 = Term.create_tty()
print(term3)

while True:
	if CommandHelper.run("killall htop") == 0 or CommandHelper.run("killall top") == 0:
		Term.print("You tough that this will be as easy as this?\n")
	time.sleep(1)
