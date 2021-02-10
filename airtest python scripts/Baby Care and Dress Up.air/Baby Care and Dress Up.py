# -*- encoding=utf8 -*-
__author__ = "Doom"

from airtest.core.api import *

#select baby

baby = Template(r"tpl1610136187762.png", record_pos=(-0.359, -0.019), resolution=(2340, 1080))
activities = [Template(r"tpl1610136238451.png", record_pos=(-0.063, -0.156), resolution=(2340, 1080)), Template(r"tpl1610136374578.png", record_pos=(-0.065, 0.088), resolution=(2340, 1080)), Template(r"tpl1610136367963.png", record_pos=(0.124, -0.165), resolution=(2340, 1080)), Template(r"tpl1610136370850.png", record_pos=(0.32, -0.162), resolution=(2340, 1080)), Template(r"tpl1610136504438.png", record_pos=(0.347, 0.083), resolution=(2340, 1080)), Template(r"tpl1610136501035.png", record_pos=(-0.063, 0.079), resolution=(2340, 1080))]


back = Template(r"tpl1610136310899.png", record_pos=(0.444, -0.201), resolution=(2340, 1080))


sleep(10) # Time for loading the game
# Banner ads
while True:
    wait(baby)
    touch(baby)
    for activity in activities:
        snapshot()
        wait(activity)
        touch(activity)
        sleep(10)
        touch(back)
    


auto_setup(__file__)