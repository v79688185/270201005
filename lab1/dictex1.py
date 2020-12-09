books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
book_Dict = dict()
for i in range(len(books)):
  keys = books[i]
  unique_charachters = len(set(keys))
  charachters = len(keys)
  value = (unique_charachters,charachters)
  book_Dict[keys] = value
print(book_Dict)
for book in books:
    charachters,unique_charachters = book_Dict[book]
    avg = (unique_charachters + charachters) /2
    book_Dict[book] = (unique_charachters,charachters,(unique_charachters + charachters)/2)
print(book_Dict) 