def observed():
  print("please enter stuff")
  observations = []
  for count in range(5):
    observation = input()
    observations.append(observation)
  return observations


def remove_observations(observations):
  want_removal = ("yes")
  while want_removal == "yes":
    print("do you want to remove any observations?")
    want_removal = input
    if (want_removal == "yes"):
      print("what do you want to remove?")
      remove = input
      remove.remove(observations)
      print("done")
    elif (want_removal == "no"):
      print("ok")

def run():
  observation = observed()
  remove_observations(observation)
  observations_set = set()
  for observation in observation:
    observations_set.add((observation, observation.count(observation)))


  
run()

