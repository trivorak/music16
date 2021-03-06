#Default Startup/Test Values test push
inCache = 'd3aca892d996d534c0fa98ae06d2a46e43836c8e'
splLen = 2         #Split Length
instCou = 3         #Instrument Count
percList = list()   #init var list

for x in range(0,instCou):
  startVar = (splLen*x)
  endVar = (startVar + splLen)
  percList.append(inCache[startVar:endVar])


print(percList)
#print(bin(int(percList[1],16)))

for x in range(0,instCou):
  print(bin(int(percList[x],16)))

# Replace hex with binary
def hex2bin(hexVal):
  return bin(int(hexVal,16))

# Remove Binary Header
def removebin(binVal):
  return binVal[2:]

# Fill Missing Binary Digits
def binfntload(binVal):
  return binVal.zfill(4*splLen)

# Reverse each index item
def revIndex(indexItem):
  return indexItem[::-1]

# Processing 
result = map(hex2bin,percList)
result = map(removebin,result)
result = map(binfntload,result)
result = map(revIndex,result)

print(list(result))

result = (result)
print(result)