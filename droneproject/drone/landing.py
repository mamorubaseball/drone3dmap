# -*- coding: UTF-8 -*-
import olympe
import time
from olympe.messages.ardrone3.Piloting import TakeOff, Landing
import os
from olympe.messages.ardrone3.Piloting import moveBy
from olympe.messages.ardrone3.PilotingState import FlyingStateChanged


DRONE_IP = os.environ.get("DRONE_IP", "192.168.42.1")


def landing():
    drone = olympe.Drone(DRONE_IP)
    drone.connect()
    assert drone(Landing()).wait().success()
    time.sleep(10)
   
if __name__ == "__main__":
    landing()