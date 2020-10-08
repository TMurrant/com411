print("Where should I look")
look = input()

if (look =="bedroom"):
  print("where in the bedroom should i look?")
  where = input()
  if (where == "under the bed"):
    print("Found some shoes but no battery")
  else:
    print("Found some mess but no battery.")


elif (look == "bathroom"):
  print("Where in the bathroom should I look?")
  where2 = input()
  if (where2 == "in the bathtub"):
    print("Found a rubber duck but no battery")
  else:
    print("Found a wet surface but no battery")


elif (look == "lab"):
  print("Where in the lab should i look")
  where3 = input()
  if (where3 == "on the table"):
    print("Yes! I have found my battery")
  else:
    print("Found some tools but no battery") 
else:
  print("I do not know where that is but I will keep looking.")