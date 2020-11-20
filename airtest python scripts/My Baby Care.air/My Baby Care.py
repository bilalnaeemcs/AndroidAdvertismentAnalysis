# -*- encoding=utf8 -*-
__author__ = "Doom"

from airtest.core.api import *

auto_setup(__file__, logdir=True)


ads = [Template(r"tpl1605747190699.png", record_pos=(-0.425, -0.937), resolution=(1080, 2340)), Template(r"tpl1605747124171.png", record_pos=(0.441, -0.934), resolution=(1080, 2340)), Template(r"tpl1605746728318.png", record_pos=(0.441, -0.946), resolution=(1080, 2340)), Template(r"tpl1605749839876.png", record_pos=(-0.157, 0.869), resolution=(1080, 2340)), Template(r"tpl1605751592460.png", record_pos=(0.415, -0.87), resolution=(1080, 2340)), Template(r"tpl1605751261268.png", record_pos=(0.413, -0.864), resolution=(1080, 2340))]

play = Template(r"tpl1605753970416.png", record_pos=(0.341, 0.35), resolution=(1080, 2340))
back = Template(r"tpl1605754269359.png", record_pos=(-0.409, 0.754), resolution=(1080, 2340))
home_btn = Template(r"tpl1605755632358.png", record_pos=(-0.397, 0.761), resolution=(1080, 2340))


children_moods = [Template(r"tpl1605754055111.png", record_pos=(0.075, -0.51), resolution=(1080, 2340)), Template(r"tpl1605754062142.png", record_pos=(-0.245, -0.22), resolution=(1080, 2340)), Template(r"tpl1605754385203.png", record_pos=(0.073, 0.154), resolution=(1080, 2340)), Template(r"tpl1605754866550.png", record_pos=(0.069, -0.517), resolution=(1080, 2340))]


# touch(play)
# sleep(3)

while True:
    for mood in children_moods:
        if exists(mood):
            touch(mood)
            wait(back)
            touch(back)
            sleep(3)

            if not exists(home_btn):
                # Take ss of the ad
                snapshot()
#                     wait 30 sec for thea dd to progress
                    sleep(30)
                # Close ad
                for btn in ads:
                    if exists(btn):
                        # take another ss of the ad
                        snapshot()
                        touch(btn)
                        wait(home_btn)
                        touch(home_btm)
                        sleep(3)
                        break







