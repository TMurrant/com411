print("how many rows should I have?")
rows = int(input())

print("How many columns should I have?")
columns = int(input())


print("Here I go:")

for row in range (0, rows, 1):
  for columns in range (0, columns, 1):
    print (":-)", end="")
    print()


print("Done")