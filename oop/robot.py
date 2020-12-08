
from inhabitant import Inhabitant

class Robot(Inhabitant):

  # class attribute
  laws = "Protect, Obey and Survive"
  
  # class (constant) attribute
  MAX_ENERGY = 100

  # A static method
  @staticmethod
  def the_laws():
    print(Robot.laws)

  # An initialiser (special instance method)
  def __init__(self, name="robot", age=0):
    super().__init__(name, age)
  # print the human class
  def __str__(self):
    return f"I am robot {self.name}"
  
if (__name__ == "__main__"):
  # create an object of type Human
    robot = Robot("brrp")

  # display the current state of the object
    print(robot)

  # invoke the method move on the object
    robot.move(10)

