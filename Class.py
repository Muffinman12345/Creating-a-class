#A class is like a big function. You can create functions in a class.
#Let's start with a "Dog" class.

class Dog:
   #This is where we make our functions. I'll start with a "bark" function
   def bark():
    return "Woof Woof!"
    #We use the return function in functions.
   #You can create multiple functions in a class
    def run():
      return "ZOOM!"
     #You can kinda add as many functions as you would like.
     def eat():
      return "Munch, Munch"
     def sleep():
      return "Yawn..."
 

#WHen we are done creating functions, we can run them.

Dog.bark()

#This would print out Woof Woof!

#The format is basically YourClassName.FunctionName()

#I'll try them all out

Dog.run()
Dog.eat()
Dog.sleep()
