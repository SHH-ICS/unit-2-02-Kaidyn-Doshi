# My Python Program
# Task:  Use the function myFunction to output a simple "Hello World!" statement
def politeGreeting(name):
  if name == "Nina":
    return("nerd emoji")
  if name == "Viridian":
    return("monkey")
  else:
    return("Hello, " + name + "!")
  if name == "bozo":
    return("bozo")
  else:
    return("Hello, " + name + "!")
name = input("Please enter your name:")        
print(politeGreeting(name))
