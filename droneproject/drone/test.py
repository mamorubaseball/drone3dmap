# -*- coding: UTF-8 -*-
import olympe
from olympe.messages.ardrone3.Piloting import TakeOff, Landing

def take_off():
    drone = olympe.Drone("192.168.42.1")
    drone.connect()
    drone(TakeOff()).wait()

