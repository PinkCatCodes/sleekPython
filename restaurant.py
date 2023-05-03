hour = 3
minute = 45


# There are plenty of places to get a
#late night bite to eat. However, they have different hours,
#so when choosing where to go, you have to think about who's
#still open!
#
#Imagine you're choosing between the following restaurants:
#
# - Barrelhouse: Closes at 11:00PM
# - Taco Bell: Closes at 2:00AM
# - Cookout: Closes at 3:00AM
# - Waffle House: Never closes. Ever.

#However, there are two wrinkles:
#
# - We're using 12-hour time.
# - hour will always represent a time from 10PM to 5AM.
#
#That means that if hour is 10 or 11, it's PM; if hour is
#12, 1, 2, 3, 4, or 5, it's AM. This will make your reasoning
#a little more complex. You may assume that all four
#restaurants open later than 6AM, though, so you don't have
#to worry about opening time, just closing time.
#
#Add some code below that will print what restaurant you'll
#go to based on the current values of hour and minute.





if hour==12 or hour==1 or hour==11:
    print("Taco Bell")
elif hour==2:
    print("Cookout")
elif hour==10:
    print("Barrelhouse")
else:
    print("Waffle House")
