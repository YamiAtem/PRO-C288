from controller import Robot
from controller import Keyboard

robot = Robot()
keyboard = Keyboard()

# create unique identifier for each device
motor_a = robot.getDevice("A motor")
motor_b = robot.getDevice("B motor")
motor_c = robot.getDevice("C motor")
motor_d = robot.getDevice("D motor")
motor_e = robot.getDevice("E motor")
motor_f = robot.getDevice("F motor")

timestep = int(robot.getBasicTimeStep())
keyboard.enable(timestep)

motor_a_pos = 0
motor_b_pos = 0
motor_c_pos = 0
motor_d_pos = 0
motor_e_pos = 0
motor_f_pos = 0

# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    key_pressed = keyboard.getKey()   
    
    if key_pressed == 49:
        motor_a_pos += 0.005
    if key_pressed == 50:
        motor_a_pos -= 0.005
    
    if key_pressed == 51:
        motor_b_pos += 0.005
    if key_pressed == 52:
        motor_b_pos -= 0.005
        
    if key_pressed == 53:
        motor_c_pos += 0.005
    if key_pressed == 54:
        motor_c_pos -= 0.005
    
    if key_pressed == 55:
        motor_d_pos += 0.005
    if key_pressed == 56:
        motor_d_pos -= 0.005
        
    if key_pressed == 57:
        motor_e_pos += 0.005
    if key_pressed == 48:
        motor_e_pos -= 0.005
    
    if key_pressed == 81:
        motor_f_pos += 0.005
    if key_pressed == 87:
        motor_f_pos -= 0.005
    
    # write code to move the joints with keyboard
    motor_a.setPosition(motor_a_pos)
    motor_b.setPosition(motor_b_pos)
    motor_c.setPosition(motor_c_pos)
    motor_d.setPosition(motor_d_pos)
    motor_e.setPosition(motor_e_pos)
    motor_f.setPosition(motor_f_pos)
    
