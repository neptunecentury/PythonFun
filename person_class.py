# Define our person class
class Person:
    name = None

    # Create a constructor method. Remember, this is called automatically when
    # a new person is created.
    def __init__(self, name):
        self.name = name

    # A person can speak some words
    def speak(self, words):
        # Say something!. If you want to include quote characters in your
        # string, you'll need to escape them with a \, or else the interpreter
        # will think you are closing the string.
        print("{0} says \"{1}\"".format(self.name, words))

Boy = Person("Eric")
Boy.speak("Hello!")

Girl = Person("Cindy")
Girl.speak("Meow!")

Man = Person("John")
Man.speak("Yay, it's Friday!")

Woman = Person("Rachel")
Woman.speak("I'm ready for the weekend!")