"""rotate controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
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


# Main loop
while robot.step(timestep) != -1:
    pass

# Enter here exit cleanup code.
