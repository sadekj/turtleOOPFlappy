import turtle
from bird import Flappy
from tube import Tube

turtle.tracer(0) # Turn off turtle mainloop (we will create our own loop)
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2 # here we get canvas(screen) width
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2 # here we get the canvas(screen) height
turtle.hideturtle() # Hide the old turtle
turtle.colormode(255)
turtle.bgcolor(78,192,202)
turtle.addshape("flappy2.gif")
turtle.addshape("flappy3.gif")
turtle.addshape("tube2.gif")
turtle.addshape("tube3.gif")

tube = Tube(350, -700, -10, 0, 104, 1080, "tube2.gif")
tube2 = Tube(350, 700, -10, 0, 104, 1080, "tube3.gif")
bird = Flappy(0, 0, 0, 0, 46, 46)

def create_background():
	turtle.clear()
	turtle.pu()
	turtle.color((93,223,114))
	turtle.begin_fill()
	turtle.goto(-SCREEN_WIDTH,-SCREEN_HEIGHT+100)
	turtle.forward(SCREEN_WIDTH*2)
	turtle.right(90)
	turtle.forward(100)
	turtle.right(90)
	turtle.forward(SCREEN_WIDTH*2)
	turtle.right(90)
	turtle.forward(100)
	turtle.right(90)
	turtle.end_fill()

def collide(blockA, blockB):
	if(blockA.right_side() >= blockB.left_side()
		and blockA.left_side() <= blockB.right_side()
		and blockA.top_side() >= blockB.bottom_side()
		and blockA.bottom_side() <= blockB.top_side()):
		return True
	else:
		return False

def upkeyPressed(event):
	bird.jump(20)

turtle.getcanvas().bind("<Up>", upkeyPressed)
turtle.getscreen().listen()
create_background()
i=0
while True:
	if(SCREEN_WIDTH != turtle.getcanvas().winfo_width()/2 or SCREEN_HEIGHT != turtle.getcanvas().winfo_height()/2):
		SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
		SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2
		create_background()
	# bird.clear()
	# tube.clear()
	# tube2.clear()
	bird.move(-SCREEN_HEIGHT)
	tube.move(SCREEN_WIDTH)
	tube2.move(SCREEN_WIDTH)
	# tube.draw_border()
	# tube2.draw_border()
	# bird.draw_border()
	if(collide(bird, tube) or collide(bird, tube2)):
		i+=1
		print "collided!"+str(i)
	turtle.getscreen().update()