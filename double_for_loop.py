
# Define a dictionary. This is basically a key value pair.
# They key is the car manufacturer, and the value is a list of available colors
animals = {'Hippos': ["baby","little","large"], 'Elephants' : ["large", "extra large"]}
for animal, options in animals.items():
    # Join the colors together with the word "and". (e.g: Red and Blue)
    colors = " or ".join(options)
    # Next, we print a line using format place holders. These allow us to
    # insert the values in the string at run time. 0 is the first, and 1 
    # comes next. So, in the format function, we put manufacture first, 
    # then our color list
    print("{0} come in {1}.".format(animal, colors))
    
    