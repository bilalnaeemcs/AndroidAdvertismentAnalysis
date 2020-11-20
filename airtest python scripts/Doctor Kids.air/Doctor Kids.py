# -*- encoding=utf8 -*-
__author__ = "Doom"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# auto_setup(__file__, logdir=True)



back1 = Template(r"tpl1605752068107.png", record_pos=(-0.369, 0.737), resolution=(1080, 2340))
back2 = Template(r"tpl1605747834511.png", record_pos=(-0.375, 0.74), resolution=(1080, 2340))
play = Template(r"tpl1605748076234.png", record_pos=(-0.094, 0.261), resolution=(1080, 2340))
ads = [Template(r"tpl1605747190699.png", record_pos=(-0.425, -0.937), resolution=(1080, 2340)), Template(r"tpl1605747124171.png", record_pos=(0.441, -0.934), resolution=(1080, 2340)), Template(r"tpl1605746728318.png", record_pos=(0.441, -0.946), resolution=(1080, 2340)), Template(r"tpl1605749839876.png", record_pos=(-0.157, 0.869), resolution=(1080, 2340)), Template(r"tpl1605751592460.png", record_pos=(0.415, -0.87), resolution=(1080, 2340)), Template(r"tpl1605751261268.png", record_pos=(0.413, -0.864), resolution=(1080, 2340))]


level_list = [Template(r"tpl1605747213831.png", record_pos=(-0.401, 0.392), resolution=(1080, 2340)), Template(r"tpl1605747217993.png", record_pos=(-0.239, 0.384), resolution=(1080, 2340)), Template(r"tpl1605747222162.png", record_pos=(-0.081, 0.383), resolution=(1080, 2340)), Template(r"tpl1605747225633.png", record_pos=(0.082, 0.38), resolution=(1080, 2340)), Template(r"tpl1605747229369.png", record_pos=(0.232, 0.385), resolution=(1080, 2340))]




# Play Button
touch(play)
sleep(2)

while True:  # --> If this while tru is commented the game will keep on playing in a loop

    # Select appropriate level
    for level in level_list:
        touch(level)
        sleep()
        # Check if an add has come up
        if not exists(Template(r"tpl1605748718715.png", record_pos=(0.006, 0.606), resolution=(1080, 2340))):
            sleep(3)
            # If a level has started go back to menu
            if exists(back1):
                touch(back1)
                break
            if exists(back2):
                touch(back2)
                break
            # if an ad comes up duting selection
            for ad in ads:
                if exists(ad):
                    snapshot()
                    # Close ad
                    touch(ad)
                    sleep(2)
                    break
            # Press back to start the level all over
            if exists(back1):
                touch(back1)
            else:
                touch(back2)
            sleep(3)
