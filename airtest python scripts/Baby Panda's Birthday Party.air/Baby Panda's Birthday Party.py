# -*- encoding=utf8 -*-
__author__ = "Doom"

from airtest.core.api import *

home_btn = Template(r"tpl1610137268377.png", record_pos=(-0.417, -0.181), resolution=(2340, 1080))
play = Template(r"tpl1610137239399.png", record_pos=(0.003, 0.111), resolution=(2340, 1080))
fish = Template(r"tpl1610137835577.png", record_pos=(-0.006, -0.067), resolution=(2340, 1080))

# sleep(10)

# touch(Template(r"tpl1610139923064.png", record_pos=(0.297, 0.086), resolution=(2340, 1080)))

while True:
    wait(play)
    touch(play)
    sleep(1)
    if exists(home_btn):
        snapshot() # for banner ad
        # make a cake and party
        touch(Template(r"tpl1610137356806.png", record_pos=(-0.303, 0.182), resolution=(2340, 1080)))
        sleep(2)
        swipe(Template(r"tpl1610137382801.png", record_pos=(-0.224, 0.191), resolution=(2340, 1080)), vector=[0.2696, -0.3353])
        sleep(2)
        swipe(Template(r"tpl1610137458035.png", record_pos=(-0.258, 0.179), resolution=(2340, 1080)), vector=[-0.0604, -0.4089])
        swipe(Template(r"tpl1610137475459.png", record_pos=(0.259, 0.179), resolution=(2340, 1080)), vector=[0.0573, -0.4166])
        sleep(2)
        swipe(Template(r"tpl1610137552071.png", record_pos=(0.247, 0.176), resolution=(2340, 1080)), vector=[-0.0619, -0.7337])
        swipe(Template(r"tpl1610137534619.png", record_pos=(-0.267, 0.182), resolution=(2340, 1080)), vector=[0.0092, -0.1691])
        sleep(2)
        swipe(Template(r"tpl1610137575876.png", record_pos=(-0.096, 0.188), resolution=(2340, 1080)), vector=[-0.1154, -0.722])
        swipe(Template(r"tpl1610140022766.png", record_pos=(0.077, 0.177), resolution=(2340, 1080)), vector=[0.1252, -0.1889])

        sleep(5)
        swipe(fish, vector=[0.0077, -0.1272])
        swipe(fish, vector=[-0.055, -0.1074])
        swipe(fish, vector=[-0.0745, 0.032])
        swipe(fish, vector=[-0.0159, 0.1516])
        swipe(fish, vector=[0.0467, 0.1668])
        swipe(fish, vector=[0.0947, -0.0152])
        sleep(7)

        # Eat Cake
        swipe(Template(r"tpl1610138187185.png", record_pos=(-0.081, -0.037), resolution=(2340, 1080)), vector=[-0.2334, 0.0664])
        for piece in range(4):
            touch((420, 479))
            sleep(1)

        swipe(Template(r"tpl1610138399501.png", record_pos=(-0.088, 0.042), resolution=(2340, 1080)), vector=[-0.2261, -0.1194])
        for piece in range(4):
            touch((420, 479))
            sleep(1)

        swipe(Template(r"tpl1610138479081.png", record_pos=(0.022, 0.051), resolution=(2340, 1080)), vector=[-0.3368, -0.1234])
        for piece in range(4):
            touch((420, 479))
            sleep(1)
        swipe(Template(r"tpl1610138514171.png", record_pos=(-0.081, -0.092), resolution=(2340, 1080)), vector=[-0.2369, 0.1859])
        for piece in range(4):
            touch((420, 479))
            sleep(1)
        swipe(Template(r"tpl1610138543194.png", record_pos=(-0.028, -0.092), resolution=(2340, 1080)), vector=[-0.2832, 0.1859])
        for piece in range(4):
            touch((420, 479))
            sleep(1)
        swipe(Template(r"tpl1610138575776.png", record_pos=(0.056, -0.104), resolution=(2340, 1080)), vector=[-0.367, 0.205])
        for piece in range(4):
            touch((420, 479))
            sleep(1)
        swipe(Template(r"tpl1610139418130.png", record_pos=(0.076, -0.035), resolution=(2340, 1080)), vector=[-0.3902, 0.0241])
        for piece in range(4):
            touch((420, 479))
            sleep(1)

        # End
        touch(home_btn)


    else:
        snapshot() # 5 sec ad for a baby panda game
        sleep(6)



auto_setup(__file__)
