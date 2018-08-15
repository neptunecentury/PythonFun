# In this example, we will reference an item in the array by its index. An index is the position the
# item is in, 0 being the first index.
candies = ["KitKat", "M&Ms", "Snickers","Pay Day", "Twix"]
# Show the options to the user, and allow them to make a selection. We will use the enumerate function
# to get each item in the array and its corresponding index
print("Please enter a selection:")
for index, candy in enumerate(candies):
    # Display the option with it's index, so the user knows what selection to make
    print("{0} - {1}".format(index, candy))

# Now, allow the user to make a selection. But what happens if they enter an invalid number?
selection = input("Which item do you want (press a number)? ")
# Convert the user's input to an integer (number) because it is a string when they type it.
# What happens if you enter "Foobar" instead? Try it!
selection = int(selection)
# Find the candy the user wants by the index they entered and store it
# in a variable called dispense. Note that if you enter a number larger
# than the number of items, you will get an error. Try it!
dispense = candies[selection]
# Tell the user the candy has been dispensed
print("Dispensing {0}. Have a nice day :)".format(dispense))

# Later, we can enhance this to check for valid user input and also keep dispensing
# until the user exits the app.
