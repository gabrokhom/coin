import pgzrun
import random

WIDTH=500
HEIGHT=500

bg=Actor('grass',(WIDTH//2,HEIGHT//2))
robot=Actor('robot_idle')
coin=Actor('coin_gold')
bomb=Actor('bomb')

def draw():
    screen.clear
    bg.draw()
    coin.draw()
    bomb.draw()
    robot.draw()











pgzrun.go()