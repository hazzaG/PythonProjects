from tone import Tone
from note import Note
p=0
p= Tone.sine(440,p, duration=1)
""""
Note("c4").play()
Note.rest(0.1)
Note("e4").play()
Note.rest(0.1)
Note("g4").play()
Note.rest(0.1)

Note.play_chord([Note("c4"),Note("e4"),Note("g4")])
"""

#Tone.create_tone_from_list([530, 660])