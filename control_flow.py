# Control FLow
# Conditional statements are used to control the flow of our program
# if, elif and else

# age = input("How old are you?")

age = 16
if age >= 15:  # If the the user is above the age of 15, allow them to buy a ticket
    print("Thank you, Please proceed to your purchase ")
elif age < 15:  # If the the user is not above the age of 15, do not allow them to buy a ticket
    print(" You may not pass")
else:  # anything else happens and no conditions are met, return this
    print("Something, went wrong, please try again later!")

# Exercise -
# As a user I would like to sell tickets according the age of the user
# and category of the movie -
# age = 12a, PG, U, 15 and 18
# user input to let us know the age to decide whether to sell the ticket or not
# casting implemented
# display the age back to the user with appropriate message

user_age = int(input("What is your age? "))
rating_U = ["Toy Story", "Finding Nemo"]
rating_PG = ["Up", "Cars"]
rating_12 = ["Transformers", "Forrest Gump"]
rating_15 = ["Deadpool", "Insidious"]
rating_18 = ["Watchmen", "The Departed"]


if int(user_age) >= 18:
    print(f"You are {user_age} years old !")
    print("This means you can buy tickets for all the films we are showing which are:")
    print(rating_U + rating_PG + rating_12 + rating_15 + rating_18)
elif int(user_age) >= 15:
    print(f"You are {user_age} years old !")
    print("This means you can buy tickets for films Rated PG, U, 12a or 15 which are:")
    print(rating_U + rating_PG + rating_12 + rating_15)
elif int(user_age) >= 12:
    print(f"You are {user_age} years old !")
    print("This means you can buy tickets for films Rated PG, U or 12a which are:")
    print(rating_U + rating_PG + rating_12)
elif int(user_age) < 12:
    print(f"You are {user_age} years old !")
    print("This means you can buy tickets for films Rated PG or U which are:")
    print(rating_U + rating_PG)
else:
    print("Something has gone wrong, please try again later!")