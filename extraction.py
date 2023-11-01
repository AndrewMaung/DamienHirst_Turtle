import colorgram
colors = colorgram.extract('hirst.jpg', 20)
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_tuple = (r, g, b)
    rgb_colors.append(rgb_tuple)

print(rgb_colors)
