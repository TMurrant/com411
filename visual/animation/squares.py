import matplotlib.pyplot as plt 
import matplotlib.animation as animation 
import numpy as np 

fig, ax = plt.subplots()

def init():
  global data 
  data = {
    "small":np.array([3,3,4,4,3]),
    "medium":np.array([2,2,5,5,2]),
    "large":np.array([1,1,6,6,1])
    
  }


def animate(frame):
  ax.set_xlim(0, 10)
  ax.set_ylim(0, 10)
  ax.plot(frame + data["small"], frame + data ["medium"], frame + data ["large"])

def run():
  global fig
  simple_animation = animation.FuncAnimation(fig, animate, frames = 720, interval = 100)

  plt.show()

run()

