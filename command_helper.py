import os
import subprocess


class CommandHelper:
	@staticmethod
	def run(cmd):
		with open(os.devnull, 'wb') as devnull:
			return subprocess.call(cmd.split(' '), stdout=devnull, stderr=subprocess.STDOUT)
