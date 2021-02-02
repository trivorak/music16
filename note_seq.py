from midiutil import MIDIFile
import math

#Default Startup/Test Values
inCache = input("Please enter a hex string: ")
noteList = list(inCache)
scaleList = [0,2,3,5,7,9,11]
rootNote = 36
midiFileName = inCache[:8]+"-m16.mid"

track = 0
channel = 0
time = 0
duration = 1
tempo = 60
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
  time = time + 1
  
with open(midiFileName, "wb") as output_file:
    MyMIDI.writeFile(output_file)

