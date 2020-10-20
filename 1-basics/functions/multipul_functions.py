def display_ladder(steps):
    # Display each step 
    for step in range(steps):
        print("| |")
        print("***") 


def create_ladder():
  print("how many steps?")
  steps = int(input())
  display_ladder(steps)


create_ladder()