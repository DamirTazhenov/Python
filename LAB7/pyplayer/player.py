import pygame as pg
import sys
pg.init()

screen = pg.display.set_mode((800,600))

music_playlist = {}
index = 0

def get_music(path):
    global music_playlist
    song = music_playlist.get(path)
    if song == None:
        canonic_path = u'LAB7/pyplayer/music/'+path
        song = pg.mixer.music.load(canonic_path)
        music_playlist[path]=song
    return(song)
get_music('1.mp3')
get_music('2.mp3')

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
            """elif event.key == pg.K_l:
                if len(music_playlist)!=0:
                    pg.mixer.music.load"""
    pg.mixer.music.load('LAB7/pyplayer/music/1.mp3')

        