#!/usr/bin/env python

from smarthouse import *

import sys

def main():
	w = Weather()
	w.open(0,0,300,300)
	w.fetch()
	w.update()

	c = Clock()
	c.open(320,0,250,20)

	sys.stdin.read(1)

	w.close()
	c.stop()


if __name__ == "__main__":
	#main()
	c = Calendar()
	c.open(0,0,500,300)
	c.update()
	sys.stdin.read(1)