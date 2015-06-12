#!/usr/bin/env python

import ovg
import time
import datetime
import threading
from .. import moduleBase


class Clock(moduleBase.Module):
	"""docstring for Clock"""

	run = True

	def open(self,x,y,w,h):
		self.run = True
		self.thread = threading.Thread(target=self._begin,args=(x,y,w,h),daemon=True)
		self.thread.start()

	def stop(self):
		self.run = False


	""" Do not call directly"""

	def _begin(self,x,y,w,h):
		super(Clock,self).open(x,y,w,h)
		ovg.clear_color(255,255,255,255)
		ovg.clear()
		self.f = ovg.create_font()
		self._update()

	def _update(self):
		start = time.time()

		ovg.clear()
		ovg.text(5,5,self.f,"{:%I:%M:%S %p %a, %b %d}".format(datetime.datetime.now()),12)
		ovg.draw()

		if self.run:
			time.sleep(1.0-(time.time() - start))
			self._update()
		else:
			ovg.cleanup()