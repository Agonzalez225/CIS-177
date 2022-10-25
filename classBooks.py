
from collections import Counter
class Book:
  
  Bookset = []
  
  def __init__(self, title, author, length, genre = None):
        self.title = title
        self.author = author
        self.length = length
        self.change_genre(genre)
        self.Bookset.append(self)
  def change_genre(self, genre):
    self.genre = genre

  def get_genre_count(self):
    genreNames = []
    for Book in self.Bookset:
      genreNames.append(Book.genre)
    return Counter(genreNames)

  def getbookset(self):
    for Book in self.Bookset:
      print(Book.title)
    
history = Book(title='US History', author='David P', length=400)
math = Book(title = "Calculus", author = "John S", length = 500, genre = "Math" )
Trig = Book(title = "Trignometry," ,author = "Andrew l ", length = 450, genre = "Math")
print(history.get_genre_count())
math.getbookset()