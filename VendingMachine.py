# In this example, we will reference an item in the array by its index. An index is the position the
# item is in, 0 being the first index.

class Candy:
    name = None
    color = None
    def __init__(self, name, color="Chocolate"):
        self.name = name
        self.color = color


candies = ["KitKat", "M&Ms", "Snickers","Pay Day", "Twix"]
machineOn = True
while machineOn:
    # Show the options to the user, and allow them to make a selection. We will use the enumerate function
    # to get each item in the array and its corresponding index
    print("Please enter a selection:")
    for index, candy in enumerate(candies):
        # Display the option with it's index, so the user knows what selection to make
        print("{0} - {1}".format(index, candy))

    # Print message to show user how to exit    
    print("Press x to quit.")

    # Now, allow the user to make a selection. But what happens if they enter an invalid number?
    selection = input("Which item do you want (press a number)? ")
    if selection == 'x':
        machineOn = False
        print("Well, maybe next time then. Bye, bye.")
    else:
        # Convert the user's input to an integer (number) because it is a string when they type it.
        selection = int(selection)
        # Find the candy the user wants by the index they entered and store it
        # in a variable called dispense. Note that if you enter a number larger
        # than the number of items, you will get an error. Try it!
        dispense = candies[selection]
        # Tell the user the candy has been dispensed
        print("Dispensing {0}. Have a nice day :)".format(dispense))
        print()

