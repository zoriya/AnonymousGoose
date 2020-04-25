#!/usr/bin/env python3
import time
import pyxhook

from term_utils import Term
from command_helper import CommandHelper
from trick import Trick


class AnonymousGoose:
	def __init__(self):
		self.should_exit = False
		self.stopped = False
		self.tricks = []
		self.keyboard_listener = pyxhook.HookManager()
		self.keyboard_listener.KeyUp = self.key_pressed
		self.keyboard_listener.HookKeyboard()
		self.keyboard_listener.start()
		Term.print_all("YOU HAVE BEEN HACKED.\n")

	def __del__(self):
		if not self.stopped:
			self.keyboard_listener.cancel()
		for trick in self.tricks:
			trick.revert()

	def run(self):
		next_trick_time = 5
		while not self.should_exit:
			try:
				if CommandHelper.run("killall htop") == 0 or CommandHelper.run("killall top") == 0:
					Term.print_all("You tough that this will be as easy as this?\n")
				time.sleep(1)
				next_trick_time -= 1
				if next_trick_time <= 0:
					trick = Trick.get_random_trick()
					next_trick_time = trick.delay
					trick.run()
					if trick.is_reversible:
						self.tricks.append(trick)
			except KeyboardInterrupt:
				...

	def key_pressed(self, key):
		if key.Ascii == 27:
			self.should_exit = True

	def stop(self):
		if self.stopped:
			return
		self.keyboard_listener.cancel()
		self.stopped = True


if __name__ == "__main__":
	goose = AnonymousGoose()
	term = Term()
	term.print("""
           `:-.......``  
           +:o+++:---::  
          `/--::/o/-+s+. 
          `/::/so/:-:-:` 
          `s:----------. 
           /:+oo//soo/o  
           `+o/://///+.  
             /do:-:m--   
             oNNmy-o`    
  `-.  `-/sdmNNNNNs`     
  sNNmmNNNNNNNNNNNNd`    
  :NNNNNNNNNNNNNNNNN-    
   -NNNNNNNNNNNNNNNd     
    oNNNNNNNNNNNNNm.     
     +NNNNNNNNNNNN/      
      oNNNNNdssmNd`      
       oNNy-   .y`       
        :o     .s        
        `s`    -sso+/`   
        `ss+:.   .-.`    
        .--:.` """"")
	goose.run()
	goose.stop()
