

slash = "/"
back_slash = "\\"
space = " "
stars = "**"
row = 1
space_count = 3 * 2 - 1

while row <= (2 * 3 - 1):
    slash_count = row
    back_slash_count = row
    print(space * space_count + slash * row + stars + back_slash * row)
    row += 1
    space_count -= 1






