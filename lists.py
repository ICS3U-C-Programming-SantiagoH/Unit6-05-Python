#!/usr/bin/env python3

# Created by: Santiago Hewett
# Created on: Dec 20, 2023
# This program will find the avg of
# numbers with user input


def calc_average(list_of_marks):
    # sum
    sum = 0

    # go through list and assign it to list_num
    for list_num in list_of_marks:
        sum += list_num

    # divide it by the length of the list
    sum = sum / len(list_of_marks)

    return sum


def main():
    # create list
    list_of_marks = []

    # display program info
    print("This program calculates the average of the numbers you insert.")

    # loop until the user wants to exit
    while True:
        try:
            # get the marks
            user_mark_int = int(
                input(
                    "Enter a mark between 0 and 100 (enter a number"
                    "less than 0 to stop): "
                )
            )

            # check if the user wants to break
            if user_mark_int < 0:
                break

            # append numbers to list
            elif user_mark_int > 100:
                # tell them the number is not valid
                print(f"{user_mark_int} is greater than 100.")
            else:
                list_of_marks.append(user_mark_int)

        # error checking
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # check if the user did not enter something
    if len(list_of_marks) == 0:
        print("Please enter a number.")

    # display the average
    else:
        # call and get avg
        average = calc_average(list_of_marks)

        # display avg
        print(f"\nAverage of marks: {average}")


if __name__ == "__main__":
    main()
