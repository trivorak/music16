from time import sleep
from psonic import *

#Default Startup/Test Values
inCache = 'cd1a15ca9c8625415891632403b401f741fbe96e'
noteList = list(inCache)

#print(noteList)
#print(len(noteList))


def lookupNote(n):
  if n == '0':
    return 36
  elif n == '1':
    return 37
  elif n == '2':
    return 38
  elif n == '3':
    return 39
  elif n == '4':
    return 40
  elif n == '5':
    return 41
  elif n == '6':
    return 42
  elif n == '7':
    return 43
  elif n == '8':
    return 44
  elif n == '9':
    return 45
  elif n == 'a':
    return 46
  elif n == 'b':
    return 47
  elif n == 'c':
    return 48
  elif n == 'd':
    return 49
  elif n == 'e':
    return 50
  elif n == 'f':
    return 51
  

for x in range(0,len(noteList)):
  play(lookupNote(noteList[x])+12)
  sleep(0.25)
  
