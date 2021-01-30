from midiutil import MIDIFile

#Default Startup/Test Values
inCache = 'd3aca892d996d534c0fa98ae06d2a46e43836c8e'
noteList = list(inCache)
scaleList = [0,2,3,5,7,9,11,12]
rootNote = 36

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
  
# for x in range(0,len(noteList)):
#     print(scaleList[lookupNote(noteList[x])%8]+rootNote)

for x in range(0,len(noteList)):
  noteReturn = lookupNote(noteList[x])
  scaleReturn = scaleList[noteReturn%8]

  if scaleReturn != noteReturn:
    rootNoteOffset = 12 + rootNote
  else:
    rootNoteOffset = rootNote

  MyMIDI.addNote(track, channel, scaleReturn+rootNoteOffset, time, duration, volume)
  time = time + 1

with open("trial_midi.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
