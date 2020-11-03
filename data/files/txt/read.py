def search (file):
  print("Searching...")
  with open(file, "r") as file:
    for line in file:
      print(f"looked in {line}")
    
  print("Done")

def run():
  search("data/files/txt/locations.txt")

run()