def short_pattern():
  pattern = {"sequences":"101", "occurrences":5}
  print(pattern)

def medium_pattern():
  pattern = {"sequence":"111000", "orrurrences": 25}
  print(pattern)

def long_pattern():
  pattern = {"sequence":"1100110011001100", "occurrences": 50}
  print(pattern)

def run(): 
  print("Analysing patterns...")
  patterns = {
    "short sequence":short_pattern(),
    "medium sequence":medium_pattern(),
    "long sequence":long_pattern()
  }
  
  for key, value in patterns.items():
    print(f"{key}: {value}")

run()