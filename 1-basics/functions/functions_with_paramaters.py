def climb_ladder(steps_taken, steps_remaining):
  if (steps_taken > steps_remaining):
    print("still some way to go")
  else:
    print("we are almost there")

climb_ladder(5, 2)
climb_ladder(2, 5)
