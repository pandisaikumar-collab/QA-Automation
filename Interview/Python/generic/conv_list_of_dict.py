colour_name = ['Black', 'White', 'Red', 'Green', 'Blue']
color_code = ['#000000', '#FFFFFF', '#FF0000', '#008000', '#0000FF']

new = []
for i, j in zip(colour_name, color_code):
    d = {'color_name': i, 'color_code': j}
    new.append(d)
print(new)

"""
Output: 
[{'color_name': 'Black', 'color_code': '#000000'}, 
{'color_name': 'White', 'color_code': '#FFFFFF'}, 
{'color_name': 'Red', 'color_code': '#FF0000'}, 
{'color_name': 'Green', 'color_code': '#008000'}, 
{'color_name': 'Blue', 'color_code': '#0000FF'}]
"""

