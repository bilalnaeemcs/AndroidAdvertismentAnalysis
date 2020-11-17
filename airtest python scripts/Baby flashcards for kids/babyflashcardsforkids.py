# -*- encoding=utf8 -*-
__author__ = "Hasan"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)



# script content
print("start...")

#simple script
#adds cover bottom of the screen throughout. No popup ads viewed in 30mins observation.
#have the game open to home screen and run

wait(Template(r"tpl1605642252916.png", record_pos=(-0.218, -0.136), resolution=(1080, 1920)))


touch(Template(r"tpl1605642252916.png", record_pos=(-0.218, -0.136), resolution=(1080, 1920)))
sleep(5)

for i in range(0,20):
    wait(Template(r"tpl1605642309817.png", record_pos=(0.358, 0.55), resolution=(1080, 1920)))
    touch(Template(r"tpl1605642309817.png", record_pos=(0.358, 0.55), resolution=(1080, 1920)))
    sleep(4)
