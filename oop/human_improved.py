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

  # An instance method
  def display(self):
    print(f"I am {self.name}")
  
  def __repr__(self):
    return f'robot(name={self.name}, age={self.age})'

if (__name__ == "__main__"):
  robot = Robot()
  robot.display()
  robot.__repr__()

class Human:

  MAX_ENERGY = 100

  def __init__(self):
    self.name = "Human"
    self.age = 0
    self.energy = Human.MAX_ENERGY

  def display(self):
    print(f"I am {self.name}")

  
  def __str__(self):
    return f'My name is {self.name} and I am {self.age} years old.'
  

if (__name__ == "__main__"):
  human = Human()
  human.__str__()
  human.display()
  
