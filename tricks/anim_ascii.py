from trick import Trick
from nian_cat import nian
from term_utils import Term
import simpleaudio as sa
import time
import threading


class AnimAsciiTrick(Trick):

	@staticmethod
	def print_anim(terminal):
		is_open = True
		musicobj = sa.WaveObject.from_wave_file("data/nian_gooz.wav")
		playobj = musicobj.play()
		terminal.print("ouioui")
		while is_open:
			for frame in nian:
				is_open = terminal.print(frame)
				time.sleep(.2)
		playobj.stop()

	@property
	def name(self):
		return "anim"

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
		thread_anim = threading.Thread(target=AnimAsciiTrick.print_anim, args=[term])
		thread_anim.setDaemon(True)
		thread_anim.start()

