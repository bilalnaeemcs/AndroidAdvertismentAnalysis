# -*- encoding=utf8 -*-
__author__ = "Doom"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


ads = [Template(r"tpl1605747190699.png", record_pos=(-0.425, -0.937), resolution=(1080, 2340)), Template(r"tpl1605747124171.png", record_pos=(0.441, -0.934), resolution=(1080, 2340)), Template(r"tpl1605746728318.png", record_pos=(0.441, -0.946), resolution=(1080, 2340)), Template(r"tpl1605749839876.png", record_pos=(-0.157, 0.869), resolution=(1080, 2340)), Template(r"tpl1605751592460.png", record_pos=(0.415, -0.87), resolution=(1080, 2340)), Template(r"tpl1605751261268.png", record_pos=(0.413, -0.864), resolution=(1080, 2340))]



play = Template(r"tpl1610121002435.png", record_pos=(0.007, 0.083), resolution=(1080, 2340))

resume = Template(r"tpl1610120497313.png", record_pos=(-0.427, 0.686), resolution=(1080, 2340))

back = Template(r"tpl1610120627032.png", record_pos=(-0.417, 0.899), resolution=(1080, 2340))


# banner ads
while True: # To play the game in loop
    # Start the game
    if exists(play):
        touch(play)
        sleep(2)
        # Resume the train movement and wait for 4 secs
        touch(resume)
        sleep(10)
        # back
        touch(back)
    # Try again in 5 seconds

    sleep(5)
    # Banner ads
    snapshot()




auto_setup(__file__)