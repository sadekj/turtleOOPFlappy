from turtle import Turtle
class Tube(Turtle):
	dx = 0
	dy = 0
	width = 0
	height = 0
	def __init__(self, x, y, dx, dy, width, height, shape):
		Turtle.__init__(self)
		self.pu()
		self.goto(x,y)
		self.dx = dx
		self.dy = dy
		self.width = width
		self.height = height
		self.shape(shape)

	def move(self, screen_width):
		newx = self.xcor() + self.dx
		newy = self.ycor() + self.dy
		if(self.right_side() < -screen_width):
			newx = screen_width+self.width/2
		self.goto(newx, newy)

	def draw_border(self):
		oldx = self.xcor()
		oldy = self.ycor()
		self.goto(self.right_side(), self.top_side())
		self.pd()
		self.right(90)
		self.forward(self.height)
		self.right(90)
		self.forward(self.width)
		self.right(90)
		self.forward(self.height)
		self.right(90)
		self.forward(self.width)
		self.pu()
		self.goto(oldx, oldy)

	def right_side(self):
		return self.xcor() + self.width/2
	def left_side(self):
		return self.xcor() - self.width/2
	def top_side(self):
		return self.ycor() + self.height/2
	def bottom_side(self):
		return self.ycor() - self.height/2