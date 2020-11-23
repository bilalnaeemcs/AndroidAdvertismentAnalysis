# -*- encoding=utf8 -*-
__author__ = "Hasan"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True)

    
# script content
print("start...")


#simple script
#adds cover bottom of the screen throughout. No popup ads viewed in 30mins observation.
#have the game open to home screen and run


wait(Template(r"tpl1605716221343.png", record_pos=(-0.019, -0.276), resolution=(1080, 1920)))
touch(Template(r"tpl1605716221343.png", record_pos=(-0.019, -0.276), resolution=(1080, 1920)))
sleep(4)


wait(Template(r"tpl1605715861087.png", record_pos=(0.009, -0.494), resolution=(1080, 1920)))
touch(Template(r"tpl1605715861087.png", record_pos=(0.009, -0.494), resolution=(1080, 1920)))
sleep(4)


wait(Template(r"tpl1605715939258.png", record_pos=(0.327, 0.145), resolution=(1080, 1920)))
touch(Template(r"tpl1605715939258.png", record_pos=(0.327, 0.145), resolution=(1080, 1920)))
sleep(4)


wait(Template(r"tpl1605715984524.png", record_pos=(-0.347, -0.188), resolution=(1080, 1920)))
touch(Template(r"tpl1605715984524.png", record_pos=(-0.347, -0.188), resolution=(1080, 1920)))
sleep(4)


wait(Template(r"tpl1605715999760.png", record_pos=(-0.337, -0.522), resolution=(1080, 1920)))
touch(Template(r"tpl1605715999760.png", record_pos=(-0.337, -0.522), resolution=(1080, 1920)))
sleep(4)


wait(Template(r"tpl1605716019811.png", record_pos=(-0.337, 0.136), resolution=(1080, 1920)))
touch(Template(r"tpl1605716019811.png", record_pos=(-0.337, 0.136), resolution=(1080, 1920)))
sleep(4)


wait(Template(r"tpl1605716035055.png", record_pos=(-0.019, 0.144), resolution=(1080, 1920)))
touch(Template(r"tpl1605716035055.png", record_pos=(-0.019, 0.144), resolution=(1080, 1920)))
sleep(4)


wait(Template(r"tpl1605716049361.png", record_pos=(0.003, 0.486), resolution=(1080, 1920)))
touch(Template(r"tpl1605716049361.png", record_pos=(0.003, 0.486), resolution=(1080, 1920)))
sleep(4)


wait(Template(r"tpl1605716144516.png", record_pos=(0.323, 0.472), resolution=(1080, 1920)))
touch(Template(r"tpl1605716144516.png", record_pos=(0.323, 0.472), resolution=(1080, 1920)))
sleep(4)


wait(Template(r"tpl1605716160244.png", record_pos=(0.337, -0.518), resolution=(1080, 1920)))
touch(Template(r"tpl1605716160244.png", record_pos=(0.337, -0.518), resolution=(1080, 1920)))
sleep(4)


wait(Template(r"tpl1605716188889.png", record_pos=(-0.423, -0.753), resolution=(1080, 1920)))
touch(Template(r"tpl1605716188889.png", record_pos=(-0.423, -0.753), resolution=(1080, 1920)))
sleep(4)










