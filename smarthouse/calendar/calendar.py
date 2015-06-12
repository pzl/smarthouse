#!/usr/bin/env python

import ovg
import time
import datetime
from .. import moduleBase


class Calendar(moduleBase.Module):
	"""docstring for Calendar"""

	_modes = ['rolling','week','month']
	_mode = 'rolling'

	dow_pad = 20
	time_pad = 25

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

		x,y,w,h = ovg.wininfo()
		quarter = int(w/4)
		d = datetime.date.today() - datetime.timedelta(days=1) #start at yesterday
		for i in range(4):
			self._drawday_vert(d+datetime.timedelta(days=i),i*quarter,quarter)

		#day of week title line
		ovg.free(ovg.draw_path(ovg.line([0,self.h-self.dow_pad],[self.w,self.h-self.dow_pad]),ovg.PaintMode.Stroke))

		self._timer()

		ovg.draw()

	def _drawday_vert(self,day,x_pos,width):
		x,y,w,h = ovg.wininfo()

		ovg.stroke(0,0,0,255)
		if day == datetime.date.today()-datetime.timedelta(days=1):
			ovg.fill(214,214,214,255)
		elif day == datetime.date.today():
			ovg.fill(242,242,212,255)
		else:
			ovg.fill(255,255,255,255)

		#square and border
		ovg.free(ovg.draw_path(ovg.rect(x_pos,0,width,h),ovg.PaintMode.Fill))
		ovg.free(ovg.draw_path(ovg.line([x_pos,0],[x_pos,h]),ovg.PaintMode.Stroke))

		ovg.fill(0,0,0,255)
		#date and day of week
		dstring = "{0:%a} {0.month}/{0.day}".format(day)
		strwidth = ovg.text_width(self.f,dstring,12)
		ovg.text( int(x_pos - strwidth/2 + width/2),h-(self.dow_pad-3),self.f,dstring,12)



	def _drawday_cal(self,day):
		pass

	def _timer(self):

		x,y,w,h = ovg.wininfo()

		ovg.stroke(0,0,0,130)
		ovg.fill(0,0,0,130)

		#timer hours right border
		ovg.free(ovg.draw_path(ovg.line([self.time_pad,0],[self.time_pad,h-self.dow_pad]),ovg.PaintMode.Stroke))

		ovg.stroke(0,0,0,20) #light stroke for hour cells

		t = datetime.datetime.now()


		cell_size = (h-self.dow_pad)/16
		font_size = 9

		for i in range(0,16):
			ovg.text(4,(h-self.dow_pad) - int( i * cell_size +font_size+1),self.f,
			         "%2d"% ( (i+8)%12 if (i+8)%12!=0 else 12 ),
			         font_size)
			tline = (h-self.dow_pad) - int( i * cell_size)
			ovg.free(ovg.draw_path(ovg.line([0,tline],[w,tline]),ovg.PaintMode.Stroke))

		tline = (h-self.dow_pad) - int(  (t.hour-8 + t.minute/60) * cell_size)
		ovg.stroke(240,50,50,90)
		ovg.free(ovg.draw_path(ovg.line([0,tline],[w,tline]),ovg.PaintMode.Stroke))
