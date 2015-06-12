#!/usr/bin/env python

import ovg
import time
import datetime
from .. import moduleBase


class Calendar(moduleBase.Module):
	"""docstring for Calendar"""

	_modes = ['rolling','week','month']
	_mode = 'rolling'

	def open(self,x,y,w,h):
		super(Calendar,self).open(x,y,w,h)
		ovg.clear_color(255,255,255,255)
		ovg.clear()
		self.f = ovg.create_font()

	def mode(self,mode):
		self._mode = mode
		self.update()

	def nextMode(self):
		index = self._modes.index(self._mode)
		index +=1
		if index >= len(self._modes):
			index = 0
		self._mode = self._modes[index]
		self.update()

	def update(self):
		"""
			Could I have made this fancy with hasattr() and callable()?
			Totally, but then you could set some cheeky modes which are
			valid methods, but not intended to be called here, like close().
			Could I have validated the list against _modes? Sure, but that's
			easily modified to include the method name too, so.. poo.
		"""
		if self._mode == 'rolling':
			self.rolling()
		elif self._mode == 'week':
			self.week()
		elif self._mode == 'month':
			self.month()
		else:
			raise Exception('invalid calendar mode setting')


	def rolling(self):
		"""Previous day, today, next 2 days"""

		dow_pad = 20
		x,y,w,h = ovg.wininfo()
		quarter = int(w/4)

		for i in range(4):
			if i == 0:
				#yesterday
				ovg.fill(214,214,214,255)
				ovg.free(ovg.draw_path(ovg.rect(i*quarter,0,quarter,h),ovg.PaintMode.Fill))
			elif i==1:
				#today
				ovg.fill(242,242,211,255)
				ovg.free(ovg.draw_path(ovg.rect(i*quarter,0,quarter,h),ovg.PaintMode.Fill))
			else:
				pass

			ovg.stroke(0,0,0,255)


			#day right black border
			ovg.free(ovg.draw_path(ovg.line([i*quarter,0],[i*quarter,h]),ovg.PaintMode.Stroke))

			#day of week title line
			ovg.free(ovg.draw_path(ovg.line([0,self.h-dow_pad],[self.w,self.h-dow_pad]),ovg.PaintMode.Stroke))

			self._timer()

			ovg.draw()

	def _timer(self):

		timer_padding = 25
		x,y,w,h = ovg.wininfo()

		ovg.stroke(0,0,0,255)
		ovg.fill(0,0,0,255)

		ovg.free(ovg.draw_path(ovg.line([timer_padding,0],[timer_padding,h]),ovg.PaintMode.Stroke))

		for i in range(1,25):
			ovg.text(4,h - int( i* (h/25+0.5) ),self.f,"%02d"%(i),9)

		t = datetime.datetime.now()
		tline = h - int(  (t.hour + t.minute/60) * (h/25+0.5) )

		ovg.stroke(240,50,50,255)
		ovg.free(ovg.draw_path(ovg.line([0,tline],[w,tline]),ovg.PaintMode.Stroke))
