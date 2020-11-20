# -*- encoding=utf8 -*-
__author__ = "Doom"

from airtest.core.api import *

auto_setup(__file__)


ads = [ Template(r"tpl1605749839876.png", record_pos=(-0.157, 0.869), resolution=(1080, 2340)), Template(r"tpl1605760470610.png", record_pos=(-0.237, 0.676), resolution=(1080, 2340)),Template(r"tpl1605759612928.png", record_pos=(-0.44, -0.956), resolution=(1080, 2340)), Template(r"tpl1605747190699.png", record_pos=(-0.425, -0.937), resolution=(1080, 2340)), Template(r"tpl1605747124171.png", record_pos=(0.441, -0.934), resolution=(1080, 2340)), Template(r"tpl1605746728318.png", record_pos=(0.441, -0.946), resolution=(1080, 2340)), Template(r"tpl1605751261268.png", record_pos=(0.413, -0.864), resolution=(1080, 2340)), Template(r"tpl1605759520159.png", record_pos=(-0.446, -0.953), resolution=(1080, 2340)), Template(r"tpl1605751592460.png", record_pos=(0.415, -0.87), resolution=(1080, 2340))]

back = Template(r"tpl1605759657311.png", record_pos=(-0.401, -0.913), resolution=(1080, 2340))

chars = [Template(r"tpl1605760408036.png", record_pos=(0.353, -0.35), resolution=(1080, 2340)), Template(r"tpl1605760828443.png", record_pos=(-0.231, 0.276), resolution=(1080, 2340)), Template(r"tpl1605759789908.png", record_pos=(0.085, -0.173), resolution=(1080, 2340)), ]


while True:
    for char in chars:
        if exists(char):
            touch(char)
            sleep(12)
            # check for ad
            if not exists(back):
                # wait for ad to progress
                sleep(5)
                for btn in ads:
                    # Keep taking snapshots of the ad at different intervals
                    snapshot()
                    if exists(btn):
                        touch(btn)
                        break
                wait(back)
                touch(back)
            else:
                touch(back)
            sleep(5)
