print("How many numbers should I sum up?")
numbers = int(input())

of = 1
total = 0
loop = numbers

while (loop > 0):
  print("please enter number", of, "of", numbers)
  number = int(input())
  of = of + 1 
  loop = loop - 1
  total = total + number


print("The answer is", total)
