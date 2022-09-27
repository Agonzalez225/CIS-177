

def addClass (classNumber, className):
  courses [classNumber] = className




courses = {}
addClass(classNumber = 87572, className = "Math" )
print(courses)



courses [74181] = 'anatomy' 
courses [65329] = 'progamming'
courses [92854] = 'history'


def courseLookup (crn):
  for key, value in courses.items():
    if key < int(crn):
      print(key)


courseLookup(crn = 82000)