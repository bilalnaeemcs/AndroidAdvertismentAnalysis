# -*- encoding=utf8 -*-
__author__ = "Doom"

from airtest.core.api import *

auto_setup(__file__, logdir=True)


# This game just has a banner ad on top and no active ads


games = [Template(r"tpl1605815103480.png", record_pos=(0.001, -0.241), resolution=(1080, 2340)), Template(r"tpl1605815513131.png", record_pos=(0.173, -0.022), resolution=(1080, 2340)), Template(r"tpl1605815812779.png", record_pos=(-0.292, -0.463), resolution=(1080, 2340)), Template(r"tpl1605815827197.png", record_pos=(-0.023, -0.51), resolution=(1080, 2340))]


play = Template(r"tpl1605815130048.png", record_pos=(0.223, -0.385), resolution=(1080, 2340)) 

pause = Template(r"tpl1605815217675.png", record_pos=(0.406, 0.971), resolution=(1080, 2340))
back = Template(r"tpl1605815243517.png", record_pos=(-0.175, -0.064), resolution=(1080, 2340)) 


while True:
    for game in games:
        wait(game)
        touch(game)
        if exists(play):
            touch(play)
        sleep(5)
        #This game has banner ads only (played 20 mins)
        snapshot()
        touch(pause)
        wait(back)
        touch(back)




