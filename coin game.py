import pgzrun
import random

WIDTH=500
HEIGHT=500
Game_over='false'
velosoty=5
timer=0
bg=Actor('grass',(WIDTH//2,HEIGHT//2))
robot=Actor('robot_idle')
coin=Actor('coin_gold')
bomb=Actor('bomb')

def start():
    global velosoty,timer,Game_over
    Game_over='false'
    velosoty=5
    timer=0
    robot.pos=WIDTH//2,HEIGHT//2
    move_bomb()
    move_coin()
    clock.schedule_interval(increment_timer,1.0)
    music.play('house')


def increment_timer():
    global timer
    timer+=1
    
    
    

     

def move_coin():
    coin.x=random.randint(20,WIDTH-20)
    coin.y=random.randint(20,HEIGHT-20)
    if coin.colliderect(robot) or coin.colliderect(bomb):
          coin.x=random.randint(20,WIDTH-20)
          coin.y=random.randint(20,HEIGHT-20)



def move_bomb():
    bomb.x=random.randint(20,WIDTH-20)
    bomb.y=random.randint(20,HEIGHT-20)
    if bomb.colliderect(robot) or bomb.colliderect(coin):
          bomb.x=random.randint(20,WIDTH-20)
          bomb.y=random.randint(20,HEIGHT-20)


def draw():
    screen.clear
    bg.draw()
    coin.draw()
    bomb.draw()
    robot.draw()


def update():
    if keyboard.left and robot.left>0:
        robot.image='robot_left'
        robot.x+=-5
    elif keyboard.right and robot.right<WIDTH:
        robot.image='robot_right'
        robot.x+=+5 
    elif keyboard.up and robot.top>0:
        robot.y-=velosoty
    elif keyboard.down and robot.bottom<HEIGHT:
        robot.y+=velosoty

    if robot.colliderect(coin):
        sounds.find_money.play()
        move_coin()
    if robot.colliderect(bomb):
        sounds.bomb_explosion.play()
        move_bomb()

def on_key_up(key):
    if key == keys.LEFT or key == keys.RIGHT:
        robot.image='robot_idle'
        












start()
pgzrun.go()