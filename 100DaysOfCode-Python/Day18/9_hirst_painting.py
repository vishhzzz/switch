# import colorgram

# colors = colorgram.extract('./Day18/image.jpg', 30)

# # each ele. is a colorgram object.
# print(type(colors[0]))

# colors_for_painting = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     print(color.rgb)

#     colors_for_painting.append((r, g, b))


# print(colors_for_painting)


import turtle, random
screen = turtle.Screen()


# we will simply store this list of colors becoz this package needs more computation, so why waste resources

color_palete = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154,41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73,43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tim = turtle.Turtle()
screen.colormode(255)

# i need to create a 10*10 square with 100 dots each with colors from color_palete
# each dot must be 20 in size and set apart at min of 50
tim.speed('fastest')
for ele in range(10):
    tim.penup()
    tim.goto(-150, 50 * ele - 150)
    tim.pendown()
    for _ in range(10):
        color = random.choice(color_palete)
        # print(color[0])
        tim.dot(20, color)
        tim.penup()
        tim.forward(50)
        tim.pendown()
    tim.penup()

screen.exitonclick()