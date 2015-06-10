#!/usr/bin/env python

import ovg

class Module(object):
	"""Base class for smarthouse modules"""

	def __init__(self):
		super(Module, self).__init__()

	def open(self,x,y,w,h):
		ovg.open(x,y,w,h)
		ovg.clear()
		

	def close(self):
		ovg.cleanup()