def observed():
  observations = []
  for count in range(7):
    observation = input()
    observations.append(observation)
  return observations

def run():
  print("counting observations")
  observations = observed()
  observations_set = set()
  for observation in observations:
    observations_set.add((observation, observations.count(observation)))

  print(observations_set)


run()