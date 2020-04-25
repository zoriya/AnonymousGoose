from trick import Trick
from nian_cat import nian
from term_utils import Term
from playsound import playsound
import time
import asyncio


class AnimAsciiTrick(Trick):
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
        playsound('data/nian_gooz.mp3', False)
        while True:
            for frame in nian:
                term.print(frame)
                time.sleep(.2)
