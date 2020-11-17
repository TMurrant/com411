import matplotlib.pyplot as plt


def read_data(file_path):
  temps = []
  file = open(file_path)
  lines = file.readlines()
  for line in lines:
    temps.append(int(line.strip()))
  file.close()
  return temps

def run():
  data = read_data("visual/subplots/temp.txt")
  fig, axes = plt.subplots(2,2)
  axes[0, 0].plot(data)
  axes[0, 1].plot(data)
  plt.show()



run()
