#!/usr/bin/env python

class Module(object):
	"""Base class for smarthouse modules"""

	def __init__(self, arg):
		super(Module, self).__init__()
		self.arg = arg

	def open(self,x,y,w,h):
		ovg.open(x,y,w,h)
		ovg.clear()
		

	def close(self):
		ovg.cleanup()