#Default Startup/Test Values
inCache = 'cd1a15ca9c8625415891632403b401f741fbe96e'
splLen = 4          #Split Length
instCou = 3         #Instrument Count
percList = list()   #init var list

for x in range(0,instCou):
  startVar = (splLen*x)
  endVar = (startVar + splLen)
  percList.append(inCache[startVar:endVar])


print(percList)






