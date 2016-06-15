'''

You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?


The other representation is a tuple of 9 integers giving local time.
The tuple items are:
  year (four digits, e.g. 1998)
  month (1-12)
  day (1-31)
  hours (0-23)
  minutes (0-59)
  seconds (0-59)
  weekday (0-6, Monday is 0)
  Julian day (day in the year, 1-366)
  DST (Daylight Savings Time) flag (-1, 0 or 1)


tt = (1900, 1, 1, 0, 0, 0, 0, 1, 0)

'''
from time import *
from calendar import monthrange

s = time()

space = 0

for yy in xrange(1901,2001):
	for mm in xrange(1,13):
#calendar.monthrange(yy,mm) > tuble of the 1st day of the month, no. of days (28~31)
#mon=0, tue=1, wed=2, thr=3, fri=4, sat=5, sun=6
		if monthrange(yy,mm)[0] == 6:
			space+=1
		
print space
print time() - s
