# Define a dictionary. This is basically a key value pair.
# They key is the car manufacturer, and the value is a list of available colors
cars = {'Volvo': ['Red', 'Green'], 'Ford' : ["Yellow", "Blue"]}

for manufacturer, options in cars.items():
    # Join the colors together with the word "and". (e.g: Red and Blue)
    colors = " and ".join(options)
    # Next, we print a line using format place holders. These allow us to
    # insert the values in the string at run time. 0 is the first, and 1 
    # comes next. So, in the format function, we put manufacture first, 
    # then our color list
    print("{0} comes in {1}".format(manufacturer, colors))
    