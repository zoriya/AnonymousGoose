from term_utils import Term
from trick import Trick


class LaughingGooseTrick(Trick):
	@property
	def name(self):
		return "Test"
	
	@property
	def delay(self):
		return 5
	
	@property
	def is_reversible(self):
		return False
	
	def revert(self):
		pass
	
	def run(self):
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
		        .--:.` """)
