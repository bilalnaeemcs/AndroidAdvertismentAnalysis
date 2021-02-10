# -*- encoding=utf8 -*-
__author__ = "Doom"

from airtest.core.api import *

ads = [Template(r"tpl1605747190699.png", record_pos=(-0.425, -0.937), resolution=(1080, 2340)), Template(r"tpl1605747124171.png", record_pos=(0.441, -0.934), resolution=(1080, 2340)), Template(r"tpl1610123860496.png", record_pos=(0.474, -0.212), resolution=(2340, 1080)), Template(r"tpl1605746728318.png", record_pos=(0.441, -0.946), resolution=(1080, 2340)), Template(r"tpl1605749839876.png", record_pos=(-0.157, 0.869), resolution=(1080, 2340)), Template(r"tpl1605751592460.png", record_pos=(0.415, -0.87), resolution=(1080, 2340)), Template(r"tpl1605751261268.png", record_pos=(0.413, -0.864), resolution=(1080, 2340))]

play = Template(r"tpl1610123921354.png", record_pos=(-0.003, -0.04), resolution=(2340, 1080))
back = Template(r"tpl1610124008836.png", record_pos=(-0.47, -0.201), resolution=(2340, 1080))

animals = [Template(r"tpl1610123950720.png", record_pos=(-0.338, 0.006), resolution=(2340, 1080)), Template(r"tpl1610123954946.png", record_pos=(-0.129, 0.018), resolution=(2340, 1080)), Template(r"tpl1610123959338.png", record_pos=(0.044, 0.015), resolution=(2340, 1080)), Template(r"tpl1610124516694.png", record_pos=(0.241, 0.031), resolution=(2340, 1080))]



# Loop starts from main screen
while True:
    for animal in animals:
        wait(play)
        touch(play)
        if not exists(animal): # an ad has started
            snapshot()
            sleep(30) # Let the ad complete for the close button to appear
            for ad in ads:
                if exists(ad):
                    touch(ad)
        wait(animal) # Ch0ose another animal
        touch(animal)
        wait(back)
        touch(back)
        sleep(2)
        touch(back)
    
    
        



auto_setup(__file__)

