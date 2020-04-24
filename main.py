#!/usr/bin/env python3
from term_utils import TermUtils
from detect_term import DetectTerm
import time

print(DetectTerm.find_terminal())
time.sleep(1)
TermUtils.print("YOU HAVE BEEN HACKED.\n")