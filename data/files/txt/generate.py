def search(File_name):
  print("searching")
  Data = {}
  section = ()
  with open(File_name) as file:
    for line in file:
      if line.startswith("Section"):
        components = line.split(":")
        section = components[1]
        Data[section] = 3
        #section.append(components[1])
      else:
        Data[line] = 1
  
  
  print("Done")

  return (Data)

def run():
  data = search("data/files/txt/books.txt")
  with open("data/files/txt/generated.txt", "w") as file:
    file.writelines(data)

      
run()
