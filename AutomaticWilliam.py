#!/usr/bin/env python

from GoogleCalendar import *

class AutomaticWilliam(object):

   def __init__(self,u,p,c):
      self._cals = GoogleCalendarMng()
      self._cals.connect (u, p)
      self._cal = self._cals.getCalendar (c)

   def ls(self):
      events = self._cal.getEvents()
      return iter(events)

   def mk(self,p,w,s,e,r): #Project, What was done, Start time, end time, rate
     self._cal.newEvent (p, w, r, s, e)

   def charges(self,s,e):
     for ev in self.ls():
        es = ev.getStartTime()
        if ( s <= es < e ):
           yield self.getEventDuration(ev)*self.getEventRate(ev)

   def getEventDuration(self,ev):
      return (ev.getEndTime() - ev.getStartTime())/3600 #the duration in hours

   def getEventRate(self,ev):
     return float(ev.getLocation())



