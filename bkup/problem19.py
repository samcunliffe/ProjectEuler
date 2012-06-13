# Project Euler Problem 19
# ========================
# You are given the following information, but you
# may prefer to do some research for yourself.

#    * 1 Jan 1900 was a Monday.
#    * Thirty days has September,
#      April, June and November.
#      All the rest have thirty-one,
#      Saving February alone,
#      Which has twenty-eight, rain or shine.
#      And on leap years, twenty-nine.
#    * A leap year occurs on any year evenly 
#      divisible by 4, but not on a century unless
#      it is divisible by 400.

# How many Sundays fell on the first of the month
# during the twentieth century (1 Jan 1901 to 31
# Dec 2000)?

dayOfWeek=1
t=0

for year in range(1900,2001):

   leapYear=False
   if (year%4==0):
      leapYear=True

   for month in range(1,13):

      if (month==4) or (month==6) or (month==9) or (month==11):
         dayRange=31
      elif (month==2) and (leapYear==False):
         dayRange=29
      elif (month==2) and (leapYear==True):
         dayRange=30
      else: 
         dayRange=32

      for day in range(1,dayRange):
         
         if (day==1) and (dayOfWeek==7) and (year!=1900):
            t+=1

         if (dayOfWeek<7):
            dayOfWeek+=1
         else:
            dayOfWeek=1
         
print t
