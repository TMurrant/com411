def directions():
  directions = ["move forward", "move backwards", "turn left", "turn right"]
  return directions 

def menu():
  print("Please enter a direction")
  directions() 
  direction = directions() 
  for index in range(len(direction)):
    print("{}:{}".format(direction[index], index))
  choice = int(input()) 
  return direction[choice] 


def run():
  route = []
  print("working out an escape route")
  loop = 5
  menu() 
  route = menu()

  while(loop > 0):
    print("Escape route {}".format(route))
    loop = loop - 1
  
run()

