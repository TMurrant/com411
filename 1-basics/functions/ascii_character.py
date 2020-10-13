print("program started")

print("please enter an ASCII code")
code = int(input())

if code in range (31, 127, 1):
  print("The ASCII code for", code,"is", (chr(code)))
else: 
  print("please enter an acceptible input")