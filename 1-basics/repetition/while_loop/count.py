print("how many live cables should I avoid")
live_cables = int(input())


while (live_cables > 0):
  print("avoiding...", live_cables,"live cables avoided")
  live_cables = live_cables - 1

print("All live cables have been avoided")