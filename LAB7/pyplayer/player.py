import pygame as pg
import sys
import os
pg.init()

screen = pg.display.set_mode((800,600))

index = 0

path = u"C:\PP2\lab7\music"
playlist = []
print ("\nplaylist:")
for filename in os.listdir(path):
    if not os.path.isdir(os.path.join(path,filename)):
        playlist.append(filename)
        print (filename)


music_playlist = {}

def get_music(path):
    global music_playlist
    song = music_playlist.get(path)
    if song == None:
        canonic_path = u'C:/PP2/lab7/music/'+path
        song = pg.mixer.music.load(canonic_path)
        music_playlist[path]=song
    return(song)

get_music(playlist[index])


done = 0
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        elif event.type == pg.KEYUP:
            if event.key == pg.K_SPACE:
                pg.mixer.music.pause()
            elif event.key == pg.K_p:
                pg.mixer.music.play()
            elif event.key == pg.K_UP:
                volume = pg.mixer.music.get_volume()
                volume+=0.3
                pg.mixer.music.set_volume(volume)
            elif event.key == pg.K_DOWN:
                volume = pg.mixer.music.get_volume()
                volume-=0.3
                pg.mixer.music.set_volume(volume)
            elif event.key == pg.K_l:
                get_music(playlist[index])
                index+=1
            elif event.key == pg.K_RIGHT and index<len(playlist)-1:
                pg.mixer.music.stop()
                index+=1
                get_music(playlist[index])
                pg.mixer.music.play()
            elif event.key == pg.K_LEFT and index>0:
                pg.mixer.music.stop()
                index-=1
                get_music(playlist[index])
                pg.mixer.music.play()