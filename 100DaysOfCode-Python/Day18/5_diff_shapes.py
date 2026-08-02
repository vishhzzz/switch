from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

'''
We need to draw:
    1. Triangle
    2. Square
    3. Pentagon
    4. Hexagon
    5. Heptagon
    6. Octagon
    7. Nonagon
    8. Decagon
'''

# *****************************************************
# class Shapes:
#     def triangle(self):
#         '''draw triagnle'''
#         for _ in range(3):
#             turtle.forward(100)
#             turtle.right(120)

#     def square(self):
#         '''draw square'''
#         for _ in range(4):
#             turtle.forward(100)
#             turtle.right(90)

#     def pentagon(self):
#         '''draw pentagon'''
#         for _ in range(5):
#             turtle.forward(100)
#             turtle.right(72)

#     def hexagon(self):
#         '''draw hexagon'''
#         for _ in range(6):
#             turtle.forward(100)
#             turtle.right(60)

#     def heptagon(self):
#         '''draw heptagon'''
#         for _ in range(7):
#             turtle.forward(100)
#             turtle.right(180-128.57)

#     def octagon(self):
#         '''draw octagon'''
#         for _ in range(8):
#             turtle.forward(100)
#             turtle.right(180-135)

#     def nonagon(self):
#         '''draw nonagon'''
#         for _ in range(9):
#             turtle.forward(100)
#             turtle.right(40)

#     def decagon(self):
#         '''draw decagon'''
#         for _ in range(10):
#             turtle.forward(100)
#             turtle.right(36)


# shapes = Shapes()
# shapes.triangle()
# shapes.square()
# shapes.pentagon()
# shapes.hexagon()
# shapes.heptagon()
# shapes.octagon()
# shapes.nonagon()
# shapes.decagon()


# *****************************************************
def draw_shape_down(no_of_sides):
    for _ in range(no_of_sides):
        turtle.forward(100)
        turtle.right(360/no_of_sides)

def draw_shape_up(no_of_sides):
    for _ in range(no_of_sides):
        turtle.forward(100)
        turtle.left(360/no_of_sides)

turtle.shape('turtle')

for no_of_sides in range(3, 11):
    draw_shape_down(no_of_sides)

turtle.backward(200)

for no_of_sides in range(3, 11):
    draw_shape_up(no_of_sides)

screen.exitonclick()