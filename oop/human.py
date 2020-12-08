# imports the inheritance class
from inhabitant import Inhabitant

class Human(Inhabitant):

   #class (constant) attribute
  MAX_ENERGY = 100

  # initialiser, passes the name and age to the inhabitant class
  def __init__(self, name="Human", age=0):
    super().__init__(name, age)
  # print the human class
  def __str__(self):
    return f"I am human {self.name}"
  
if (__name__ == "__main__"):
  # create an object of type Human
  human = Human("Jeff")

  # display the current state of the object
  print(human)

  # invoke the method move on the object
  human.move(10)





  