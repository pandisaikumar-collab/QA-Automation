nested_list = [[1,2], [3,4],[5,6]]

flatten_list = []
for sublist in nested_list:
    flatten_list += sublist
    # or use extend method -- flatten_list.append(sublist)

print(flatten_list)

