import os

def cwd():
  path = os.getcwd()
  print(f"Current Working Folder Path: {path}")
  print("The folder contains the following")
  for file in os.listdir(path):
    print(file)

def run():
  print("proccessing...")
  cwd() 

run()