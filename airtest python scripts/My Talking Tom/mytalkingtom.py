# -*- encoding=utf8 -*-
__author__ = "Hasan"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=[
            "android://127.0.0.1:5037/192.168.123.104:5555?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=ADBTOUCH",
    ])


# script content
print("start...")

#to run, open and enter the app

#checks if there is an ad available.
if exists(Template(r"tpl1605521139828.png", record_pos=(0.395, 0.312), resolution=(1080, 1920))) or exists(Template(r"tpl1605521900006.png", record_pos=(0.395, 0.312), resolution=(1080, 1920)))
:
    touch(Template(r"tpl1605521139828.png", record_pos=(0.395, 0.312), resolution=(1080, 1920)))
    touch(Template(r"tpl1605521900006.png", record_pos=(0.395, 0.312), resolution=(1080, 1920)))

sleep(35)
#check for exit button
if exists(Template(r"tpl1605521273027.png", record_pos=(-0.433, -0.824), resolution=(1080, 1920))):
    touch(Template(r"tpl1605521273027.png", record_pos=(-0.433, -0.824), resolution=(1080, 1920)))

if exists(Template(r"tpl1605521550795.png", record_pos=(0.429, -0.814), resolution=(1080, 1920))):
    touch(Template(r"tpl1605521550795.png", record_pos=(0.429, -0.814), resolution=(1080, 1920)))

#the game always makes us spin a wheel after ad. so script will do that.
sleep(10)
if exists(Template(r"tpl1605521638098.png", record_pos=(0.001, 0.506), resolution=(1080, 1920))):
    touch(Template(r"tpl1605521638098.png", record_pos=(0.001, 0.506), resolution=(1080, 1920)))

#now close the prize wheel window.
if exists(Template(r"tpl1605521708774.png", record_pos=(0.403, -0.818), resolution=(1080, 1920))):
    touch(Template(r"tpl1605521708774.png", record_pos=(0.403, -0.818), resolution=(1080, 1920)))

#"daily offer" ad popup
if exists(Template(r"tpl1605521831086.png", record_pos=(0.294, -0.358), resolution=(1080, 1920))):
    touch(Template(r"tpl1605521831086.png", record_pos=(0.294, -0.358), resolution=(1080, 1920)))

#done, run script again for new ad

    
    
    
    
    
    
    
    
    
    
    
