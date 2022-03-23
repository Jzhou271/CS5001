import turtle
import math


screen = turtle.Screen()
screen.bgcolor('black')
ellipse = turtle.Turtle()
ellipse.speed(0)
ellipse.color('lightcoral')


def draw_ellipse(a, b, angle, steps, rotate):
    """
    This is the function to draw ellipse on the screen, repeated 25 times in
    lightcoral color.
    :param: int or float, major axis of ellipse
    :param: int or float, minor axis of ellipse
    :param: int or float, angle of ellipse associated with the next one
    :param: int or float, moved steps of ellipse
    :param: int or float, angle of next point
    :return: lightcoral ellipse in rotate degree, repeated 25 times
    """
    min_angle = (2 * math.pi / 360) * angle / steps
    ellipse.penup()
    ellipse.setpos(b * math.sin(rotate), -b * math.cos(rotate))
    ellipse.pendown()
    for i in range(steps):
        point = [a * math.sin((i + 1) * min_angle),
                 -b * math.cos((i + 1) * min_angle)]
        point = [point[0] * math.cos(rotate) - point[1] * math.sin(rotate),
                 point[0] * math.sin(rotate) + point[1] * math.cos(rotate)]
        ellipse.setpos(point)


for i in range(25):
    draw_ellipse(180, 90, 360, 50, (i + 1) * 10)


diamond = turtle.Turtle()
diamond.speed(0)
diamond.color('paleturquoise')


def draw_diamond(length, angle):
    """
    This is the function to draw a diamond on the screen in paleturquoise color
    4 side of diamond are equaled 
    :param: int or float, length of one side
    :param: int or float, interior angle of smaller angle in diamond
    :return: none
    """
    angle = 360 / 50
    length = 80
    for i in range(50):
        diamond.forward(length)
        diamond.left(angle)
        diamond.forward(length)
        diamond.left(180 - angle)
        diamond.forward(length)
        diamond.left(angle)
        diamond.forward(length)
        diamond.left(180 - angle)
        diamond.left(angle)


def draw_diamond_repeat(length, angle, repeat):
    """
    This is the function to draw diamond 100 times, with 36 rotated degree
    :param: int or float, length of one side
    :param: int or float, interior angle of smaller angle in diamond
    :param: int or float, draw diamonds for one round
    :return: paleturquoise diamonds for one round, repeatd 100 times
    """
    for i in range(repeat):
        draw_diamond(length, angle)


draw_diamond_repeat(diamond, 100, 1)
yellow_sun = turtle.Turtle()
yellow_sun.speed(0)
yellow_sun.color('yellow')


def draw_inner_circle(t, size):
    """
    This is the function to draw 1 circle in yellow color
    :param: string, draw a circle
    :param: int or float, size of the circle
    :return: none
    """
    t.circle(size)


def draw_inner_circle_repeat(t, size, repeat):
    """
    This is the function to draw circles for one round. circles in yellow
    color 60 and repeat 60 times
    :param: string, draw a circle
    :param: int or float, size of the circle
    :param: int or float, circles to draw in one round
    :return: yellow circles in one round, repeated 50 times
    """
    for i in range(repeat):
        draw_inner_circle(t, size)
        t.right(360 / repeat)


draw_inner_circle_repeat(yellow_sun, 50, 50)
ring = turtle.Turtle()
ring.speed(0)


def ring_circle(r, color):
    """
    This is the function to draw ring circles, has gap between the former ring
    circle and current ring circle. repeated and displayed as cross of one
    blue and one lime color
    :param: int or float, the radius of circle
    :param: color, cross of one blue and one lime
    :return: ring circles, repeatd 15 times, has the gap between each circle
    """
    ring.penup()
    ring.goto(0, -r)
    ring.pendown()
    ring.circle(r)


max_r = 150
gap = max_r / 50
ring_circle(max_r, 'lime')
current_r = max_r - gap
for i in range(15):
    current_r = current_r - gap
    if i % 2 == 0:
        ring.color('blue')
        ring_circle(current_r, 'blue')
    else:
        ring.color('lime')
        ring_circle(current_r, 'lime')        


turtle.done()
