import matplotlib.pyplot as plt

def coordinate():
  print("please enter the x values")
  x = int(input())
  print("please enter the y values")
  y = int(input())
  values = (x, y)
  return values 

def path():
  print("retrieving path...")
  x_values = []
  y_values = []

  for count in range(4):
    data = path() 
    x_values.append(data[0])
    y_values.append(data[1])
  
  return[x_values, y_values]

  


def run():
  values = path()
  plt.plot(values, "ro--")
  plt.show()

run()




  
 



