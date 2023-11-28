#!/usr/bin/env python3

# Created by: Noah Smith
# Created on: Nov. 20th, 2023
# This program asks the user to enter a whole number
# then tells the user every factor of that number


def main():
    # Greeting
    print("")
    print("This program finds all the factors of the whole number you enter.")
    print("For example, 6 has the factors 1, 2, 3, and 6.")
    print("")

    # Get the whole number
    user_num_string = input("Enter a whole number: ")

    # Making sure the number is an integer
    try:
        user_num_int = int(user_num_string)

        if user_num_int == 0:
            print("0 is a factor of 0.")

        # Check if the number is negative
        elif user_num_int < 0:
            print("{} is not a whole number.".format(user_num_int))

        # For loop to find all the factors of the user's number
        for counter in range(1, (user_num_int + 1)):
            factor = user_num_int % counter
            if factor == 0:
                print("{} is a factor of {}.".format(counter, user_num_int))
            elif (user_num_int < counter):
                break
    except:
        # If the user did not enter an integer
        print("{} is not an integer!".format(user_num_string))
    finally:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
