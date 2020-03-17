import mido


mid = mido.MidiFile()
track = mido.MidiTrack()
mid.tracks.append(track)

#bpm = \frac{60000000}{tempo}
def music(note,base_num,base_time):
    
    #meta_time = 60 * 60 * 10 / bpm
    major_notes = [0, 2, 2, 1, 2, 2, 2, 1]
    base_note = 60
    track.append(mido.Message('note_on', note=base_note+base_num*12 + sum(major_notes[0:note]), velocity=96, time=0,channel=1))
    track.append(mido.Message('note_off', note=base_note+base_num*12 + sum(major_notes[0:note]), velocity=96, time=int(480*base_time),channel=1))
    #track.append(mido.Message('note_on', note=base_note, velocity=96, time=0))
    #track.append(mido.Message('note_off', note=base_note, velocity=96, time=480*base_time))
    
def lemon_music():
    #1
    music(1,1,0.5)
    music(2,1,0.5)

    music(3,1,1)
    music(1,1,0.5)
    music(6,0,1.5)
    music(2,1,1)

    music(7,0,1)
    music(5,0,0.5)
    music(3,0,1.5)
    music(7,0,1)

    music(6,0,1)
    music(5,0,0.5)
    music(1,0,1.5)
    music(5,0,1)

    music(3,0,3)
    #2
    music(2,0,0.5)
    music(3,0,0.5)

    music(4,0,2)
    #
    music(1,1,1)
    music(7,0,0.5)
    music(1,1,0.5)

    music(5,0,2)
    music(4,0,1)
    music(3,0,0.75)
    music(4,0,0.25)

    music(4,0,2)
    #
    music(1,1,1)
    music(7,0,0.5)
    music(6,0,0.5)

    music(5,0,3)
    #
    music(1,1,0.5)
    music(2,1,0.5)

    music(3,1,1)
    music(1,1,0.5)
    music(6,0,1.5)
    music(2,1,1)

    music(7,0,1)
    music(5,0,0.5)
    music(3,0,1.5)
    music(7,0,1)

    music(6,0,1)
    music(5,0,0.5)
    music(1,0,1.5)
    music(5,0,1)

    music(3,0,3)
    #
    music(2,0,0.5)
    music(3,0,0.5)

    music(4,0,2)
    #
    music(5,0,1)
    music(4,0,0.5)
    music(5,0,0.5)

    music(3,0,1)
    music(5,0,1)
    music(1,1,1)
    music(3,1,1)

    music(2,1,1.5)
    music(2,1,0.5)
    music(2,1,0.5)
    music(1,1,1)
    music(1,1,0.5)

    music(1,1,4)
    #加空白
    track.append(mido.Message('note_on', note=0, velocity=0, time=0))
    track.append(mido.Message('note_off', note=0, velocity=0, time=480*7))

    
    music(1,1,0.5)
    music(2,1,0.5)

    music(3,1,1)
    music(1,1,0.5)
    music(6,0,1.5)
    music(2,1,1)

    music(7,0,1)
    music(5,0,0.5)
    music(3,0,1.5)
    music(7,0,1)

    music(6,0,1)
    music(5,0,0.5)
    music(1,0,1.5)
    music(5,0,1)

    music(3,0,3)

    #
    music(2,0,0.5)
    music(3,0,0.5)

    music(4,0,2)
    #
    music(1,1,1)
    music(7,0,0.5)
    music(1,1,0.5)

    music(5,0,2)
    music(4,0,1)
    music(3,0,0.75)
    music(4,0,0.25)

    music(4,0,2)
    #
    music(1,1,1)
    music(7,0,0.5)
    music(6,0,0.5)

    music(5,0,3)
    #
    music(1,1,0.5)
    music(2,1,0.5)

    music(3,1,1)
    music(1,1,0.5)
    music(6,0,1.5)
    music(2,1,1)

    music(7,0,1)
    music(5,0,0.5)
    music(3,0,1.5)
    music(7,0,1)

    music(6,0,1)
    music(5,0,0.5)
    music(1,0,1.5)
    music(5,0,1)

    music(3,0,3)
    #
    music(2,0,0.5)
    music(3,0,0.5)

    music(4,0,2)
    music(5,0,1)
    music(4,0,0.5)
    music(5,0,0.5)

    music(3,0,1)
    music(5,0,1)
    music(1,1,1)
    music(3,1,1)

    music(2,1,0.5)
    music(2,1,1.5)
    music(2,1,0.75)
    music(1,1,1.25)

    music(1,1,4)
    #
    music(6,0,1.5)
    music(7,0,0.5)
    music(1,1,1)
    music(7,0,0.5)
    music(6,0,0.5)

    music(5,0,1)
    music(3,1,1)
    music(3,1,2)
    #

    music(2,1,1.5)
    music(3,1,0.5)
    music(4,1,1)
    music(3,1,0.5)
    music(2,1,0.5)

    music(1,1,1)
    music(2,1,1)
    music(5,0,2)
    #
    music(4,0,1.5)
    music(5,0,0.5)
    music(6,0,1)
    music(5,0,0.5)
    music(4,0,0.5)
    
    music(3,0,1)
    music(1,1,1)
    music(1,1,1)
    music(1,1,1)

    #
    music(7,0,2)
    music(6,0,1)
    music(7,0,1)

    music(1,1,1)
    #加空白
    track.append(mido.Message('note_on', note=0, velocity=0, time=0))
    track.append(mido.Message('note_off', note=0, velocity=0, time=480*1))
    music(2,1,0.75)
    music(3,1,0.25)
    music(2,1,0.75)
    music(1,1,0.25)

    music(6,0,0.5)
    music(1,1,1.5)
    music(3,1,0.75)
    music(5,1,1.25)#/

    music(2,1,0.5)
    music(1,1,1.5)
    #
    music(2,1,0.75)
    music(3,1,0.25)
    music(2,1,0.75)
    music(1,1,0.25)

    music(6,0,0.5)
    music(1,1,1.5)
    music(3,1,0.75)
    music(5,1,1.25)

    music(2,1,0.5)
    music(1,1,1.5)
    #
    music(2,1,0.75)
    music(3,1,0.25)
    music(2,1,0.75)
    music(1,1,0.25)

    music(6,0,0.5)
    music(1,1,1.5)
    music(3,1,0.75)
    music(5,1,1.25)#\

    music(5,1,0.125)
    music(6,1,0.375)
    music(5,1,1.5)

    music(5,1,0.5)
    music(1,2,1.5)

    music(7,1,0.5)
    music(5,1,1.5)
    music(3,1,0.5)
    music(5,1,1)
    music(2,1,0.5)

    music(2,1,2)
    #
    music(2,1,0.75)
    music(3,1,0.25)
    music(2,1,0.75)
    music(1,1,0.25)

    music(6,0,0.5)
    music(1,1,1.5)
    music(3,1,0.75)
    music(5,1,1.25)
    #
    music(2,1,0.5)
    music(1,1,1.5)
    music(1,1,0.75)
    music(1,1,0.25)
    music(2,1,0.75)
    music(3,1,0.25)

    music(4,1,0.75)
    music(3,1,1.25)#\
    music(3,1,0.125)
    music(2,1,0.875)#\
    music(7,0,1)

    music(1,1,3)
    #
    music(1,1,0.75)
    music(7,0,0.25)

    music(6,0,1)
    music(7,0,1)
    music(1,1,1)
    music(2,1,1)

    music(1,1,1)
    music(5,0,1)
    music(3,0,1)#\
    music(5,0,1)

    music(6,0,0.75)
    music(2,1,1.25)
    music(7,0,0.75)
    music(1,1,1.25)

    music(1,1,3)
    music(1,1,0.75)
    music(7,0,0.25)

    music(6,0,1)
    music(7,0,1)
    music(1,1,1)
    music(2,1,1)

    music(1,1,1)
    music(5,0,1)
    music(1,1,1)#\
    music(2,1,1)

    music(3,1,0.75)
    music(4,1,1.25)
    music(2,1,0.75)
    music(1,1,1.25)

    music(1,1,3)
    #Kongbai
    #
    music(3,1,1)
    music(1,1,1)
    music(5,1,1)
    music(1,1,1)
    music(1,1,1)
    music(2,1,1)
    music(5,1,1)
    music(1,1,1)
    music(1,1,1)
    music(2,1,1)
    music(5,1,1)
    music(1,1,1)
    music(1,1,1)
    music(2,1,1)
    music(3,1,1)
    music(1,1,1)
    music(2,1,2)
    music(5,1,1)
    music(1,1,1)
    music(1,1,1)
    music(2,1,1)
    music(5,1,1)
    music(1,1,1)
    music(2,1,2)
    music(1,1,2)
    music(2,1,3)
    music(1,1,0.5)
    music(2,1,0.5)

    music(3,1,1)
    music(1,1,0.5)
    music(6,0,1.5)
    music(2,1,1)

    music(7,0,1)
    music(5,0,0.5)
    music(3,0,1.5)
    music(7,0,1)

    music(6,0,1)
    music(5,0,0.5)
    music(1,0,1.5)
    music(5,0,1)

    music(3,0,3)

    #
    music(2,0,0.5)
    music(3,0,0.5)

    music(4,0,2)
    #
    music(1,1,1)
    music(7,0,0.5)
    music(1,1,0.5)

    music(5,0,2)
    music(4,0,1)
    music(3,0,0.75)
    music(4,0,0.25)

    music(4,0,2)
    #
    music(1,1,1)
    music(7,0,0.5)
    music(6,0,0.5)

    music(5,0,3)
    #
    music(1,1,0.5)
    music(2,1,0.5)

    music(3,1,1)
    music(1,1,0.5)
    music(6,0,1.5)
    music(2,1,1)

    music(7,0,1)
    music(5,0,0.5)
    music(3,0,1.5)
    music(7,0,1)

    music(6,0,1)
    music(5,0,0.5)
    music(1,0,1.5)
    music(5,0,1)

    music(3,0,3)
    #
    music(2,0,0.5)
    music(3,0,0.5)

    music(4,0,2)
    music(5,0,1)
    music(4,0,0.5)
    music(5,0,0.5)

    music(3,0,1)
    music(5,0,1)
    music(1,1,1)
    music(3,1,1)

    music(2,1,0.5)
    music(2,1,1.5)
    music(2,1,0.75)
    music(1,1,1.25)

    music(1,1,4)
    #
    music(6,0,1.5)
    music(7,0,0.5)
    music(1,1,1)
    music(7,0,0.5)
    music(6,0,0.5)

    music(5,0,1)
    music(3,1,1)
    music(3,1,2)
    #

    music(2,1,1.5)
    music(3,1,0.5)
    music(4,1,1)
    music(3,1,0.5)
    music(2,1,0.5)

    music(1,1,1)
    music(2,1,1)
    music(5,0,2)
    #
    music(4,0,1.5)
    music(5,0,0.5)
    music(6,0,1)
    music(5,0,0.5)
    music(4,0,0.5)
    
    music(3,0,1)
    music(1,1,1)
    music(1,1,1)
    music(1,1,1)

    #
    music(7,0,2)
    music(6,0,1)
    music(7,0,1)

    music(1,1,1)
    #加空白
    track.append(mido.Message('note_on', note=0, velocity=0, time=0))
    track.append(mido.Message('note_off', note=0, velocity=0, time=480*1))
    music(2,1,0.75)
    music(3,1,0.25)
    music(2,1,0.75)
    music(1,1,0.25)

    music(6,0,0.5)
    music(1,1,1.5)
    music(3,1,0.75)
    music(5,1,1.25)#/

    music(2,1,0.5)
    music(1,1,1.5)
    #
    music(2,1,0.75)
    music(3,1,0.25)
    music(2,1,0.75)
    music(1,1,0.25)

    music(6,0,0.5)
    music(1,1,1.5)
    music(3,1,0.75)
    music(5,1,1.25)

    music(2,1,0.5)
    music(1,1,1.5)
    #
    music(2,1,0.75)
    music(3,1,0.25)
    music(2,1,0.75)
    music(1,1,0.25)

    music(6,0,0.5)
    music(1,1,1.5)
    music(3,1,0.75)
    music(5,1,1.25)#\

    music(5,1,0.125)
    music(6,1,0.375)
    music(5,1,1.5)

    music(5,1,0.5)
    music(1,2,1.5)

    music(7,1,0.5)
    music(5,1,1.5)
    music(3,1,0.5)
    music(5,1,1)
    music(2,1,0.5)

    music(2,1,2)
    #
    music(2,1,0.75)
    music(3,1,0.25)
    music(2,1,0.75)
    music(1,1,0.25)

    music(6,0,0.5)
    music(1,1,1.5)
    music(3,1,0.75)
    music(5,1,1.25)
    #
    music(2,1,0.5)
    music(1,1,1.5)
    music(1,1,0.75)
    music(1,1,0.25)
    music(2,1,0.75)
    music(3,1,0.25)

    music(4,1,0.75)
    music(3,1,1.25)#\
    music(3,1,0.125)
    music(2,1,0.875)#\
    music(7,0,1)

    music(1,1,3)
    #
    music(1,1,0.75)
    music(7,0,0.25)

    music(6,0,1)
    music(7,0,1)
    music(1,1,1)
    music(2,1,1)

    music(1,1,1)
    music(5,0,1)
    music(3,0,1)#\
    music(5,0,1)

    music(6,0,0.75)
    music(2,1,1.25)
    music(7,0,0.75)
    music(1,1,1.25)

    music(1,1,3)
    music(1,1,0.75)
    music(7,0,0.25)

    music(6,0,1)
    music(7,0,1)
    music(1,1,1)
    music(2,1,1)

    music(1,1,1)
    music(5,0,1)
    music(1,1,1)#\
    music(2,1,1)

    music(3,1,0.75)
    music(4,1,1.25)
    music(2,1,0.75)
    music(1,1,1.25)

    music(1,1,3)
    #Kongbai
    #
    music(1,1,2)
    music(1,1,1.75)
    music(4,0,0.25)
    music(1,1,2)
    music(7,0,2)

    music(1,1,2)
    music(5,1,2)

    music(6,1,2)
    music(5,1,2)

    music(2,1,2)
    music(4,1,2)

    music(3,1,4)

    music(1,1,2)
    music(3,1,2)

    music(4,1,2)
    music(3,1,2)
    
    music(2,1,2)
    music(7,0,2)

    music(1,1,4)

    music(1,1,2)
    music(5,1,2)

    music(6,1,2)
    music(5,1,2)

    music(2,1,2)
    music(4,1,1)
    music(3,1,1)

    music(3,1,4)

    music(1,1,2)
    music(3,1,2)

    music(4,1,2)
    music(3,1,2)

    music(2,1,2)
    music(7,0,2)

    music(1,1,2)
    #kongbai

    music(6,0,1)
    music(7,0,0.5)

    music(1,1,2)
    music(5,1,2)

    music(6,1,2)
    music(5,1,1)
    music(2,1,1)

    music(2,1,2)
    music(4,1,1)
    music(3,1,1)

    music(3,1,4)

    music(1,1,2)
    music(3,1,2)

    music(4,1,2)
    music(3,1,2)

    music(2,1,2)
    music(7,0,2)

    music(1,1,3)
    music(6,0,0.5)
    music(7,0,0.5)

    music(1,1,2)
    music(5,1,2)

    music(6,1,2)
    music(5,1,2)

    music(7,1,2)
    music(7,1,1)
    music(1,2,1)

    music(1,2,4)

    music(1,2,2)
    music(5,1,2)

    music(4,1,2)
    music(3,1,1)
    music(2,1,1)

    music(2,1,2)
    music(2,1,2)

    music(6,0,2)
    music(1,1,1)
    music(3,2,1)

    music(4,2,4)
    music(4,2,1)
    music(5,2,1)
    music(5,2,1)
    music(6,1,1)
    music(4,2,4)
    music(4,1,1)
    #kongbai
    music(2,1,0.75)
    music(3,1,0.25)
    music(2,1,0.75)
    music(1,1,0.25)

    music(6,0,0.5)
    music(1,1,1.5)
    music(3,1,0.75)
    music(5,1,1.25)#/

    music(2,1,0.5)
    music(1,1,1.5)
    #
    music(2,1,0.75)
    music(3,1,0.25)
    music(2,1,0.75)
    music(1,1,0.25)

    music(6,0,0.5)
    music(1,1,1.5)
    music(3,1,0.75)
    music(5,1,1.25)

    music(2,1,0.5)
    music(1,1,1.5)
    #
    music(2,1,0.75)
    music(3,1,0.25)
    music(2,1,0.75)
    music(1,1,0.25)

    music(6,0,0.5)
    music(1,1,1.5)
    music(3,1,0.75)
    music(5,1,1.25)#\

    music(5,1,0.125)
    music(6,1,0.375)
    music(5,1,1.5)

    music(5,1,0.5)
    music(1,2,1.5)

    music(7,1,0.5)
    music(5,1,1.5)
    music(3,1,0.5)
    music(5,1,1)
    music(2,1,0.5)

    music(2,1,2)
    #
    music(2,1,0.75)
    music(3,1,0.25)
    music(2,1,0.75)
    music(1,1,0.25)

    music(6,0,0.5)
    music(1,1,1.5)
    music(3,1,0.75)
    music(5,1,1.25)
    #
    music(2,1,0.5)
    music(1,1,1.5)
    music(1,1,0.75)
    music(1,1,0.25)
    music(2,1,0.75)
    music(3,1,0.25)

    music(6,1,0.75)
    music(3,1,1.25)#\
    music(3,1,0.125)
    music(2,1,0.875)#\
    music(7,0,1)

    music(1,1,3)
    #
    music(1,1,0.75)
    music(7,0,0.25)

    music(6,0,1)
    music(7,0,1)
    music(1,1,1)
    music(2,1,1)

    music(1,1,1)
    music(5,0,1)
    music(3,0,1)#\
    music(5,0,1)

    music(6,0,0.75)
    music(2,1,1.25)
    music(7,0,0.75)
    music(1,1,1.25)

    music(1,1,3)
    music(1,1,0.75)
    music(7,0,0.25)

    music(6,0,1)
    music(7,0,1)
    music(1,1,1)
    music(2,1,1)

    music(1,1,1)
    music(5,0,1)
    music(4,0,1)
    music(3,1,1)

    music(4,1,0.75)
    music(1,1,1.25)
    music(1,1,0.75)
    music(5,1,1.25)

    music(3,1,3)
    music(3,1,0.75)
    music(2,1,0.25)

    music(1,1,1)
    music(2,1,1)
    music(3,1,1)
    music(4,1,1)

    music(3,1,1)
    music(1,1,1)
    music(5,0,1)
    music(3,0,1)

    music(2,1,0.75)
    music(3,1,1.25)
    music(2,1,0.75)
    music(1,1,1.25)

    music(1,1,2)
    music(4,-2,0.25)
    music(1,-1,0.25)
    music(4,-1,0.25)
    music(5,-1,0.25)
    music(1,0,0.25)
    music(2,0,0.25)
    music(5,0,0.25)
    music(1,1,0.25)

    music(2,1,0.25)
    music(5,1,0.25)
    music(1,2,0.25)
    music(2,2,0.25)
    music(5,2,0.25)
    music(1,3,0.75)
    music(1,1,0.5)
    music(5,1,1.5)
    music(1,1,0.5)
    music(5,1,1.5)
    music(1,1,0.5)
    music(5,1,1.5)
    music(1,1,0.5)
    music(5,1,1.5)
    music(1,1,0.5)
    music(5,1,1.5)
    music(1,1,0.5)
    music(5,1,3.5)




    



lemon_music()

mid.save('a2.mid')