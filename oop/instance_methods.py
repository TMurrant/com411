class Robot:

  # A class attribute
  laws = "Protect, Obey and Survive"

  # A class method
  def the_laws(self):
    print(Robot.laws)

  # An initialiser (special instance method)
  def __init__(self):

    # An instance attribute
    self.name = "Robot"
    self.age = 0
  
  def age(self):
    self.age += 1
  
  

  # An instance method
  def display(self):
    print(f"I am {self.name}")

if (__name__ == "__main__"):
  robot = Robot()
  robot.display()

class Human:

  MAX_ENERGY = 100

  def __init__(self, name=0, age=0, weight=0):
    self.name = "Human"
    self.age = age
    self.energy = Human.MAX_ENERGY

  def age(self):
    self.age += 1
  
  def eat(self):
    self.energy += 10
  
  def move(self):
    self.energy -= 35

  def display(self):
    print(f"I am {self.name}, I hame {self.age} years old and my energy is {self.energy}")

if (__name__ == "__main__"):
  human = Human()
  human.display()
