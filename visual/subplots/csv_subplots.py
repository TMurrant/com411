import csv
import matplotlib.pyplot as plt

def read_data():
  
  with open("visual/subplots/weeks.csv") as csvfile:
    csv_reader = csv.reader(csvfile)
    header = next(csv_reader)
    temps = {}
    temps = {
      header = [0].strip():[]
      header = [1].strip():[]
    }
    for row in csv_reader:
      temps[header[0]].append(row[0].strip())
      temps[header[1]].append(row[0].strip())
    return temps

def run():
  data = read_data()
  fig, axes = plt.subplots(2, 2)

  axes[0, 0].plot(data)
  axes[0, 1].plot(data)

  plt.show()

run()





