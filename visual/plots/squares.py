import matplotlib.pyplot as plt

def small():
  x = [3,4,3,4]
  y = [3,3,4,4]
  
  plt.plot(x, y, "o-")


def medium():
  x = [5,5,2,2]
  y = [2,5,5,2]

  plt.plot(x, y, "s-")


def large():
  x = [1,6,1,6]
  y = [1,6,6,1]

  plt.plot(x, y, "yo")



small()
medium() 
large()
plt.show()