print()
infinite_loop = 1
# Create something that equals 1 (or anything), then make the loop true.
while infinite_loop == 1:
    # Creating the nested loop, to make it an infinite, make sure the statement within it is true.
    # Indent it like normal.

    print()
    number = input('Enter a number you would to see in binary form:  ')
    print()
    # Getting the number which you need to convert.
    decimal = int(number)
    # Making number turn into a integer (int).
    binary = ''
    # Creating an empty space for the list of answers to be stored.
    # Indent the loop within the loop.
    while decimal != 0:
        # This loop makes it so it keeps dividing the number until it reaches 0.
        remainder = decimal % 2
        # The remainder is equal to the decimal being %2. (the remainder of that number)
        binary += str(remainder)
        # This adds the remainders onto the binary list, so it remembers the answer after each divide.
        decimal = int(decimal / 2)
        # Gets how many times the number can be divided by two (but not the remainder)
    final_binary = binary[::-1]
    # This reverses the list, look on OneNote for notes on the different types to use of this.
    # Couldn't use reversed(binary) or binary.reverse as it is a str (plus its easier as [::-1]
    print("The binary is: " + (str(final_binary)))
    # Prints out the final answer to the code.
    #
    #
    print()
    #
    #
    print("Another conversion, but in int form...")
    print()
    #
    #
    # Another and much easier way to do this using int, instead of str.
    number = int(input("Please enter a number: "))
    print()
    print("The binary is: " + (bin(number)[2:]))
    # The bin() function converts it without the need for the while loop. Much nicer to use.
    # The [2:0] makes the first 2 numbers/letters of the sequence skipped, and only states the binary.
    # Otherwise it would start with 0b, this is called slicing.
