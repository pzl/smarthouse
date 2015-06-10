#!/usr/bin/env python

from smarthouse import *

import sys

def main():
	w = Weather()
	w.open(0,0,300,300)
	w.fetch()
	w.update()

	sys.stdin.read(1)

	w.close()


if __name__ == "__main__":
	main()