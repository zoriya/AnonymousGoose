import os
import subprocess


class CommandHelper:
	@staticmethod
	def run(cmd):
		with open(os.devnull, 'wb') as devnull:
			return subprocess.call(cmd.split(' '), stdout=devnull, stderr=subprocess.STDOUT)

	@staticmethod
	def run_async(cmd):
		with open(os.devnull, 'wb') as devnull:
			return subprocess.Popen(cmd.split(' '), stdout=devnull, stderr=subprocess.STDOUT)
