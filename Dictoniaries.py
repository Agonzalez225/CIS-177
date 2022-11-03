

family = {

   'Loui': {'Birthday':"01/20/00",'Fav Color':'blue', 'Fav artist': 'Eminem'},
   'Alberto':  {'Birthday':"05/23/01",'Fav Color':'Green', 'Fav artist': 'drake'},
   'Walter':  {'Birthday':"08/28/96",'Fav Color':'Red', 'Fav artist': 'drake'},
  'Emma':  {'Birthday':"01/13/02",'Fav Color':'purple', 'Fav artist': 'kanye'},
  
}

family["Ashley"] = {"Fav color": "Pink", "Birthday": "11/02/02"}

name_comes_first = 'ZZZZZZ'

for name in family.keys():
    if name < name_comes_first:
        name_comes_first =name 

print(name_comes_first)
print(family[name_comes_first])