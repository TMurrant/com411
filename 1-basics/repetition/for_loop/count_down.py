print("How far are we from the cave?")
far_from_cave = int(input())

steps = far_from_cave + 0

for count in range (0,far_from_cave,1):
  print(steps,"steps from cave")
  steps = steps - 1 

print("we have reached the cave")