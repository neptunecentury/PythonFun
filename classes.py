# A class is a self contained object that can have properties and functions. You can create
# as many instances of the class as you want and assign different attributes to each one.

class Cat:
    # We are just defining some variables here, but they have no value, hence None
    # The name of our cat
    name = None
    # The color of our cat
    color = None

    # Define an initializer method. This method is called automatically when we create
    # a new instance of a Cat. This method has an optional parameter called color. If
    # we don't pass it, it will default to Black
    def __init__(self, name, color="Black"):
        # self is the variable that contains the information in this class. So,
        # if we want to populate some default values, we can do that here.
        self.name = name
        self.color = color
        

    # Let's define a pur method. Methods inside classes pass in a default parameter called self.
    # this let's the function access variables in the class
    def pur(self):
        print("{0} says purrrrrrrrrrrrrrrrrrrrr".format(self.name))

    # Let's define a meow method
    def meow(self):
        print("{0} says meow".format(self.name))

    # Let's define an eat method
    def eat(self):
        print ("{0} says nom nom nom".format(self.name))
#End Class - I miss code blocks :(

# OK, now lets create a cat and give it a name!
# Since this __init__ method has an optional parameter called color. We
# don't have to specify the color.
myCat = Cat("Meowster")

# The cat can pur and meow. We call a method like so:
myCat.pur()
myCat.meow()
myCat.eat()

# What color is the cat?
print("{0} is a {1} cat.".format(myCat.name, myCat.color))

# OK, now lets create another cat and give it a name and a paint job!
myOtherCat = Cat("Big Fluffy", "Pink")

# The cat can pur and meow
myOtherCat.pur()
myOtherCat.meow()
myOtherCat.eat()

# What color is the cat?
print("{0} is a {1} cat.".format(myOtherCat.name, myOtherCat.color))

# Let's say I found a kitten.
kitten = Cat("Jingles", "Purple")

# The kitten can pur and meow
kitten.pur()
kitten.meow()
kitten.eat()

# Let's introduce her to the world!
print("Hello world! I am {0}, the {1} kitten!".format(kitten.name, kitten.color))
# Let's define an array of cats! It's empty, because we are going to add
# cats to it in a loop. Let's get 10 cats!
crazyCats = []
for index in range(10):
    # Create a new cat and just name it cat 0, cat 1, etc... We won't worry about
    # color. They're all black cats
    newCat = Cat("Cat {0}".format(index))
    crazyCats.append(newCat)

# Let's make them all meow!
for cat in crazyCats:
    cat.meow()
    cat.eat()

