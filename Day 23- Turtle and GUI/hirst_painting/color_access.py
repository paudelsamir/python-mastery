import colorgram

rgb_colors = []
colors = colorgram.extract('Day 18- Turtle and GUI/hirst_painting/image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)

print(rgb_colors)  