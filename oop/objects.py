
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

if (__name__ == "__main__"):
  robot = Robot()
  robot.display()

class Human:

  MAX_ENERGY = 100

  def __init__(self):
    self.name = "Human"
    self.age = 0
    self.energy = Human.MAX_ENERGY

  def display(self):
    print(f"I am {self.name}")

if (__name__ == "__main__"):
  human = Human()
  human.display()



class planet:
  
  humans = []
  robots = []

  def add_human(self, human):
    self.humans.append(human)
  
  def remove_human(self, human):
    self.humans.remove(human)
  
  def add_robot(self, robot):
    self.robots.append(robot)
  
  def remove_robot(self, robot):
    self.robots.append(robot)
  
  planet = humans()
  planet.display()