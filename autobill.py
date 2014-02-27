#!/usr/bin/env python

who = 'beth.marston@gmail.com'
pw  = 'zfmqgthkrimeuzsh'
cal = 'medextra-hours'

form   = '%Y.%m.%d'
since  = "2013.06.06"
until  = "2013.07.06"

from AutomaticWilliam import *

#hello Google
aw = AutomaticWilliam(who, pw, cal)

#parse times into timestamps
def mkchron(stamp,form):
   return time.mktime(time.strptime(stamp,form))

since = mkchron(since,form)
until = mkchron(until,form)

#the big number
print sum(aw.charges(since,until))
