def sum_weights(beep, bop):
  total_weight = beep + bop
  return total_weight

def calc_avg_weights(beep, bop):
  avg_weight = (beep + bop) / 2
  return avg_weight

def run():
  print("please enter beeps weight")
  beep = float(input())
  print("please enter bops weight")
  bop = float(input())
  print("sum or average")
  decision = input()
  if decision == ("sum"):
    answer = sum_weights(beep, bop)
    print("The sum weight is", answer)
  elif decision == ("average"):
    answer = calc_avg_weights(beep, bop)
    print("The average weight is", answer)
  else:
    print("I am not sure what you would like to do.")

run()


