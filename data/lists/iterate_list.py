def directions():
  directions = ["move forward", "move backwards", "turn left", "turn right"]
  return directions 

def menu():
  print("please select a direction:")
  direction = directions()
  for index in range(len(direction)):
    print("{}:{}".format(direction[index], index))
    
  
def run():
  menu()

run()