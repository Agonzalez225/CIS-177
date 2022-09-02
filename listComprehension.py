print([num **3 for num in list(range(1,11))])


flipResult = ["heads", "tails" ]

[[print(flip1+flip2) for flip2 in flipResult] for flip1 in flipResult]
  
def onlyvowels(word):
  letters = []
  [letters.append (letter) if letter in ["a","e","i","o","u"] else None for letter in word]
  return letters
print(onlyvowels("997phone991"))


print([x+y for x in [10,20,30] for y in [1,2,3]])

for x in [10,20,30]: 
  for y in [1,2,3]:
    print(x+y)
  
# we add 10 to the numbers 1, 2, 3
# next we 20 to the numbers 1, 2, 3
# lastly we add 30 to the numbers 1, 2, 3

  
    
    
   