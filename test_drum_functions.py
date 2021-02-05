inCache = '12a32f4561bc6a123546951abcdef'
splLen = 4         #Split Length
instCou = 3         #Instrument Count
percList = list()   #init var list

for x in range(0,instCou):
  startVar = (splLen*x)
  endVar = (startVar + splLen)
  percList.append(inCache[startVar:endVar])

# Replace hex with binary
def hex2bin(hexVal):
  return bin(int(hexVal,16))

# Remove Binary Header
def removeBin(binVal):
  return binVal[2:]

# Fill Missing Binary Digits
def binFntLoad(binVal):
  return binVal.zfill(4*splLen)

# Reverse each index item
def revIndex(indexItem):
  return indexItem[::-1]

def hex2drumBin(inputVal):
  return revIndex(binFntLoad(removeBin(hex2bin(inputVal))))

print(hex2drumBin(percList[1]))
