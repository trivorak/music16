from psonic import *

perc1 = list('11001011')
perc2 = list('00110101')
perc3 = list('00010101')

for x in range(0, 40):
  if int(perc1[x % len(perc1)]) == 1:
    sample('kick.wav')

  if int(perc2[x % len(perc2)]) == 1:
   	sample('snare.wav')

  if int(perc3[x % len(perc3)]) == 1:
   	sample('chh.wav')

  sleep(.5)

