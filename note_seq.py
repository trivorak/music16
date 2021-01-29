from psonic import *
from midiutil import MIDIFile

#Default Startup/Test Values
inCache = 'd3aca892d996d534c0fa98ae06d2a46e43836c8e'
noteList = list(inCache)

track = 0
channel = 0
time = 0
duration = 1
tempo = 60
volume = 100

MyMIDI = MIDIFile(1)
MyMIDI.addTempo(track,time,tempo)

def lookupNote(n):
  return 36 + int(n,16)
  
for x in range(0,len(noteList)):
  MyMIDI.addNote(track, channel, lookupNote(noteList[x]), time, duration, volume)
  time = time + 1

with open("trial_midi.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
