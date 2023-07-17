import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    color_list = []
    for _ in color.rgb:
        color_list.append(_)
    rgb_colors.append(tuple(color_list))
print(rgb_colors)

