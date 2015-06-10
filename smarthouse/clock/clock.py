#!/usr/bin/env python

import ovg
import time
import datetime
import sys


def tick():
	start = time.time()

	ovg.clear()
	ovg.text(5,5,"{:%I:%M %p %a, %b %d}".format(datetime.datetime.now()),12)
	ovg.draw()

	time.sleep(60.0-(time.time()-start))
	tick()


def main():
	ovg.open(500,0,300,20)
	tick()





if __name__ == "__main__":
    main()
