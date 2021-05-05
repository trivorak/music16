from midiutil import MIDIFile
import math

#Hex String Input
inCache = input("Please enter a hex string: ")

#Input Prompt
majorScale = [0,2,4,5,7,9,11]
naturalMinorScale = [0,2,3,5,7,8,10]
harmonicMinorScale = [0,2,3,5,7,8,11]
melodicMinorScale = [0,2,3,5,7,9,11]
dorianScale = [0,2,3,5,7,9,10]
locrianScale = [0,1,3,4,7,8,10]
lydianScale = [0,2,4,6,7,9,11]
mixolydianScale = [0,2,4,5,7,9,10]
phrygianScale =[0,1,3,5,7,8,10]
pentatonicMajorScale = [0,2,4,7,9]
pentatonicMinorScale = [0,3,5,7,10]

listOfScales = [majorScale,naturalMinorScale,harmonicMinorScale,melodicMinorScale,dorianScale,locrianScale,lydianScale,mixolydianScale,phrygianScale,pentatonicMajorScale,pentatonicMinorScale]

print(" 0 - Major")
print(" 1 - Natural Minor")
print(" 2 - Harmonic Minor")
print(" 3 - Melodic Minor")
print(" 4 - Dorian")
print(" 5 - Locrian")
print(" 6 - Lydian")
print(" 7 - Mixolydian")
print(" 8 - Phrygian")
print(" 9 - Pentatonic Major")
print("10 - Pentatonic Minor")
print("--------------------------------------")
print("Please Select Your Scale (0 - 10):    ")

scaleSelect = input("")


#Default Startup/Test Values
noteList = list(inCache)
scaleList = listOfScales[int(scaleSelect,10)]
rootNote = 36
midiFileName = inCache[:8]+".mid"

track = 0
channel = 0
time = 0
duration = 0.25
tempo = 110
volume = 100

MyMIDI = MIDIFile(1)
MyMIDI.addTempo(track,time,tempo)

def lookupNote(n):
  return int(n,16)

rootNote = lookupNote(inCache[0]) + rootNote

for x in range(0,len(noteList)):
  noteReturn = lookupNote(noteList[x])
  scaleReturn = scaleList[noteReturn%len(scaleList)]
  
  rootNoteOffset = (math.floor(noteReturn / len(scaleList))*12)+rootNote

  MyMIDI.addNote(track, channel, scaleReturn+rootNoteOffset, time, duration, volume)
  time = time + 0.25
  
with open(midiFileName, "wb") as output_file:
    MyMIDI.writeFile(output_file)

