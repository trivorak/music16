from midiutil import MIDIFile

track = 0
channel = 0
time = 0
duration = .25
tempo = 60
volume = 100

MyMIDI = MIDIFile(1)
MyMIDI.addTempo(track,time,tempo)


perc1 = list('11001011')
perc2 = list('00110101')
perc3 = list('00010101')



for x in range(0, len(perc1)):
  if int(perc1[x]) == 1:
     MyMIDI.addNote(track, channel, 36, time, duration, volume)

  if int(perc2[x]) == 1:
   	MyMIDI.addNote(track, channel, 38, time, duration, volume)

  if int(perc3[x]) == 1:
   	MyMIDI.addNote(track, channel, 42, time, duration, volume)
  time = time + .5


with open("drums.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)