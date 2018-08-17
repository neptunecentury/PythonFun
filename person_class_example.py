# Here, we will import the Person class from the person_class file. If we had multuple things
# to import in the person_class file, we could use import *, but this should be used with caution-You
# might end up importing two methods or classes with the same name, and one would overwrite the other.
from person_class import Person

def run():
    # Make a new person
    frank = Person("Frank")
    # Make frank say something
    frank.speak("Hi, I'm an instance of a Person object. Whoo hooo!")

    Boy = Person("Eric")
    Boy.speak("Hello!")

    Girl = Person("Cindy")
    Girl.speak("Meow!")

    Man = Person("John")
    Man.speak("Yay, it's Friday!")

    Woman = Person("Rachel")
    Woman.speak("I'm ready for the weekend!")

# Run the app
run()
