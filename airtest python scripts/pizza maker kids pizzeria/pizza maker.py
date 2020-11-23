# -*- encoding=utf8 -*-
__author__ = "Hasan"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)



# script content
print("start...")

# must have game open on menu for the script to work

wait(Template(r"tpl1605546333778.png", record_pos=(0.243, 0.634), resolution=(1080, 1920)))
touch(Template(r"tpl1605546333778.png", record_pos=(0.243, 0.634), resolution=(1080, 1920)))
sleep(5)

touch(Template(r"tpl1605544538417.png", record_pos=(-0.341, 0.71), resolution=(1080, 1920)))
sleep(5)

touch(Template(r"tpl1605544223009.png", record_pos=(0.301, 0.338), resolution=(1080, 1920)))
sleep(5)

touch(Template(r"tpl1605544247312.png", record_pos=(-0.339, 0.386), resolution=(1080, 1920)))
sleep(5)

touch(Template(r"tpl1605544326768.png", record_pos=(-0.13, 0.386), resolution=(1080, 1920)))
sleep(5)

touch(Template(r"tpl1605544345254.png", record_pos=(0.055, 0.372), resolution=(1080, 1920)))
sleep(5)

touch(Template(r"tpl1605544366062.png", record_pos=(0.373, -0.284), resolution=(1080, 1920)))
sleep(5)

touch(Template(r"tpl1605544424098.png", record_pos=(0.173, -0.57), resolution=(1080, 1920)))
sleep(5)

#given 40secs for human interference so user has to press the spoon and move it around a bit
sleep(30)

touch(Template(r"tpl1605549448492.png", record_pos=(0.315, 0.598), resolution=(1080, 1920)))
sleep(5)

swipe(Template(r"tpl1605549673047.png", record_pos=(-0.007, -0.21), resolution=(1080, 1920)), vector=[0.004, -0.2518])
sleep(5)













