from midiutil import MIDIFile
import math

#Default Startup/Test Values

inCache = 'd3aca892d996d534c0fa98ae06d2a46e43836c8e'
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
  
for x in range(0,len(noteList)):
  noteReturn = lookupNote(noteList[x])
  scaleReturn = scaleList[noteReturn%len(scaleList)]
  
  rootNoteOffset = (math.floor(noteReturn / len(scaleList))*12)+rootNote

  MyMIDI.addNote(track, channel, scaleReturn+rootNoteOffset, time, duration, volume)
  time = time + 1
  print(scaleReturn+rootNoteOffset)
  
with open(midiFileName, "wb") as output_file:
    MyMIDI.writeFile(output_file)

