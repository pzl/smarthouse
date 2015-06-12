#!/usr/bin/env python

from smarthouse import *

import sys

def main():
	w = Weather()
	w.open(5,5,300,300)
	w.fetch()
	w.update()

	c = Calendar()
	c.open(330,5,500,300)
	c.update()

	"""
	cl = Clock()
	cl.open(320,0,250,20)
	"""

	sys.stdin.read(1)

	w.close()
	c.close()
	#cl.stop()


if __name__ == "__main__":
	main()
