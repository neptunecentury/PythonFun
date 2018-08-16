# Methods or Functions can help make our code reusable and organized.
# We'll define a Run method to store all our application's code, and in turn, that method
# will call other functions to do stuff.
def Run():
    # This is our main application code
    print("Hello! Welcome to the wonderful world of functions!")

    # Call a function that adds some numbers!
    value = Add(3,5)
    print("The function returned {0}".format(value))
    # Call the same function again with different args!
    value = Multiply(68,785)
    print("The function returned {0}".format(value))
    # The above two print statements are exactly the same... maybe they
    # should be in a function too. Maybe something called, ShowValue

    # We can also do some weird stuff with functions ;)
    DoMath(Add)
    DoMath(Multiply)


# Define a function that will return us the sum of two numbers
# We have two arguments, or values that we can pass into our
# function when we call it. The function can then use those
# values and do stuff with them.
def Add(num1, num2):
    # A return statement tells the function to give a value back to the caller.
    # The caller is what statement made the function call.
    return num1 + num2

# Multiply two numbers
def Multiply(num1, num2):
    # Return the product
    return num1 * num2

# Functions can also be passed as arguments. These are often referred to as "CallBacks"
# This is a little more advanced, but extremely powerful.
def DoMath(someFunc):
    # This method just calls whatever function you passed as an argument. It doesn't
    # care what it is.
    value = someFunc(7,56)
    # We can use a special built in property (__name__) to get the name of the function as well.
    print("The {0} function returned {1}".format(someFunc.__name__, value))
    


# Down here, we simply call Run. This function will then call other functions
Run()
