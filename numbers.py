my_int = -6

# Check to see whether the value of my_int is even or odd, and
# whether it's positive or negative.
#
# - If it's even and positive, print "Evenly positive".
# - If it's even and negative, print "Evenly negative".
# - If it's odd and positive, print "Oddly positive".
# - If it's odd and negative, print "Oddly negative".
#
# You may assume the number will not be 0.



# checking for even number
if my_int % 2 == 0 and my_int > 0:
    print("Evenly positive")

elif my_int % 2 == 0 and my_int < 0:
    print("Evenly negative")

elif not my_int % 2 == 0 and my_int < 0:
    print("Oddly negative")

elif not my_int % 2 == 0 and my_int > 0:
    print("Oddly positive")