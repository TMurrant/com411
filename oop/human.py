<<<<<<< HEAD
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
=======
#class Robot:

  # A class attribute
 # laws = "Protect, Obey and Survive"

  # A class method
 # def the_laws(self):
  #  print(Robot.laws)

  # An initialiser (special instance method)
 # def __init__(self):

    # An instance attribute
  #  self.name = "Robot"
   # self.age = 0

  # An instance method
 # def display(self):
  #  print(f"I am {self.name}")

#if (__name__ == "__main__"):
 # robot = Robot()
 # robot.display()

#class Human:

 # MAX_ENERGY = 100

 # def __init__(self):
    #self.name = "Human"
    #self.age = 0
   # self.energy = Human.MAX_ENERGY

  #def display(self):
 #   print(f"I am {self.name}")

#if (__name__ == "__main__"):
  #human = Human()
 # human.display()

>>>>>>> 4e77b22fa9d8bac293f1d0275055f74da5c6345a


<<<<<<< HEAD



  
=======
  # class (constant) attribute
  MAX_ENERGY = 100

  # initialiser
  def __init__(self, name="Human", age=0):
    self.name = name
    self.age = age
    self.energy = Human.MAX_ENERGY

  # magic methods
  def __repr__(self):
    return f'human(name={self.name}, age={self.age}, energy={self.energy})'

  def __str__(self):
    return f'My name is {self.name} and I am {self.age} years old and my energy is {self.energy}.'

  # instance methods
  def display(self):
    print(f"I am {self.name}")

  def grow(self):
    self.age += 1

  def eat(self, amount):
    potential_energy = self.energy + amount
    if (potential_energy > Human.MAX_ENERGY):
      self.energy = Human.MAX_ENERGY
      return potential_energy - self.energy
    else:
      self.energy = potential_energy
      return 0

  def move(self, distance):
    potential_energy = self.energy - distance
    if (potential_energy < 0):
      self.energy = 0
      return self.energy - abs(potential_energy)
    else:
      self.energy = potential_energy
      return 0


if (__name__ == "__main__"):
  human = Human()
  print(repr(human))
  human.move(10)
  print(repr(human))
  human.eat(5)
  print(repr(human))
  human.eat(20)
  print(repr(human))
>>>>>>> 4e77b22fa9d8bac293f1d0275055f74da5c6345a
