import colorgram

colors = colorgram.extract('./Day18/image.jpg', 30)

# each ele. is a colorgram object.
print(type(colors[0]))

colors_for_painting = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    print(color.rgb)

    colors_for_painting.append((r, g, b))


print(colors_for_painting)


# we will simply store this list of colors becoz this package needs more computation, so why waste resources
