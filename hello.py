
someNames = ['Apple', 'Car', 'Banana']
for name in someNames:
    print(name)

# This is a comment. Ask the user which is their favorite
fav = input("Which one is your favorite? ")
# Convert the user's response to lower case so that it is easy
# to test what they said.
fav = fav.lower()
# The below code checks what your favorite is and then responds.
if fav == 'apple':
    print("Hey! That's my favorite too! \\o/")
    print("You're the best!")
elif fav == 'car':
    print("Cars are cool, I guess...")
else:
    print("Sorry, I don't understand.")