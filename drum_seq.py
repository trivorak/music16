from midiutil import MIDIFile

track = 0
channel = 0
time = 0
duration = .25
tempo = 60
volume = 100

MyMIDI = MIDIFile(1)
MyMIDI.addTempo(track,time,tempo)

inCache = input(str("Please enter a hex string: "))
splLen = 4          #Split Length
instCou = 3         #Instrument Count
percList = list()   #init var list
midiFileName = inCache[:8]+"_drum.mid"

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

# Make 3 Vars
perc1 = list(hex2drumBin(percList[0]))
perc2 = list(hex2drumBin(percList[1]))
perc3 = list(hex2drumBin(percList[2]))

# Print Test
print(perc1)
print(perc2)
print(perc3)

for x in range(0, len(perc1)):
  if int(perc1[x]) == 1:
     MyMIDI.addNote(track, channel, 36, time, duration, volume)

  if int(perc2[x]) == 1:
   	MyMIDI.addNote(track, channel, 38, time, duration, volume)

  if int(perc3[x]) == 1:
   	MyMIDI.addNote(track, channel, 42, time, duration, volume)
  time = time + .5


with open(midiFileName, "wb") as output_file:
    MyMIDI.writeFile(output_file)