
import pygame as pg
def play_music(music_file):

  clock = pg.time.Clock()
  try:
    pg.mixer.music.load(music_file)
    print("Music file {} loaded!".format(music_file))
  except pygame.error:
    print("File {} not found! {}".format(music_file, pg.get_error()))
    return
  pg.mixer.music.play()

  while pg.mixer.music.get_busy():
    clock.tick(30)

music_file = "a2.mid"#pywork1保存的midi文件名

freq = 44100  
bitsize = -16  
channels = 2  
buffer = 2048  
pg.mixer.init(freq, bitsize, channels, buffer)

pg.mixer.music.set_volume(0.8)
try:
  play_music(music_file)
except KeyboardInterrupt:

  pg.mixer.music.fadeout(1000)
  pg.mixer.music.stop()
  raise SystemExit