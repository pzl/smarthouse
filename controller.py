#!/usr/bin/env python

from multiprocessing import Process

import sys
import time

def weather_widget():
	from smarthouse import Weather
	w = Weather()
	w.open(5,5,300,300)
	w.fetch()
	w.update()
	time.sleep(30)
	w.close()



def cal_widget():
	from smarthouse import Calendar
	c = Calendar()
	c.open(330,5,500,300)
	c.update()
	time.sleep(30)
	c.close()

def main():
	w = Process(target=weather_widget)
	c = Process(target=cal_widget)
	w.start()
	c.start()

	sys.stdin.read(1)



if __name__ == "__main__":
	main()
