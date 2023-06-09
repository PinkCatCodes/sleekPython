rating = "R"
age = 6


# Imagine that
# you are a parent who decides on the following rules:
#
# - Any child can see a G-rated movie.
# - To see a PG-rated movie, your child must be 8 or older.
# - To see a PG-13-rated movie, your child must be 13 or older.
# - To see an R-rated movie, your child must be 17 or older.
# - Your child may never see an NC-17 movie.
#
# The variables above give a rating and a child's age. Use
# these variables to select and print one of these two
# messages based on the criteria above:
#
# - "You may see that movie!"
# - "You may not see that movie!"
#
# However, there's one trick: you may not use the 'and' operator
# anywhere in this code!


# Add your code here!
if rating == "G":
    print("You may see that movie!")

elif rating == "PG":
    if age >= 8:
        print("You may see that movie!")
    else:
        print("You may not see that movie!")

elif rating == "PG-13":
    if age >= 13:
        print("You may see that movie!")
    else:
        print("You may not see that movie!")

elif rating == "R":
    if age >= 17:
        print("You may see that movie!")
    else:
        print("You may not see that movie!")

elif rating == "NC-17":
    print("You may not see that movie!")