def search(file_name):
  print("searching")
  sections = []
  books = []
  with open(file_name)as file:
    for line in file:
      if line.startswith("Section"):
        components = line.split(":")
        sections.append(components[1])
      else:
        books.append(line)
  print("done")
  return (sections, books)

def save(file_name, tuple):
  print("saving")
  with open(file_name, "w") as file:
      file.write("sections:")
      for line in tuple[0]:
        file.write(line)
      file.write("\n")
      file.write("Books:")
      for book in tuple[1]:
        file.write(book)
  print("Done!")

def run():
 data = search("data/files/txt/books.txt")
 save("data/files/txt/section-books.txt", data)

run()
  

 


        


      