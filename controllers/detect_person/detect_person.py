#!/usr/local/opendr/venv/bin/python3
"""detect_person controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor

import sys
sys.path.append("./src/")

from opendr.perception.object_detection_2d import YOLOv3DetectorLearner
from opendr.engine.datasets import ExternalDataset
from controller import Robot

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())


left_motor = robot.getDevice("wheel_left_joint")
right_motor = robot.getDevice("wheel_right_joint")
left_motor.setPosition(float("+inf"))
right_motor.setPosition(float("+inf"))
left_motor.setVelocity(2.0)
right_motor.setVelocity(-2.0)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

# Enter here exit cleanup code.
