import seaborn as sns


palette = sns.color_palette("colorblind")
color_names = ['dark_blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'grey', 'yellow', 'light_blue']
colors = {}
for i, color in enumerate(palette):
    colors[color_names[i]] = color
