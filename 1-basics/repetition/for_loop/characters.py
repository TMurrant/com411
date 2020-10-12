print("What strange marking do you see?")
marking = input()

print("Identifying...")

place = 0
letter = 0 

for postiion in range(0, len(marking), 1):
  print("index", place,":", marking[letter])
  place = place + 1 
  letter = letter + 1 
print("Done!")