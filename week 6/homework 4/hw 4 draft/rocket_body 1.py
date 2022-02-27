
row = 0
size_n = 10
n = size_n
vertical_bar = "|"
slash = "/"
backslash = "\\"
dot = "."

while row < size_n + n:
    print(vertical_bar + dot * row + (backslash + slash) * size_n + dot * row
          + dot * row + (backslash + slash) * size_n + dot * row + vertical_bar)
    row += 1
    size_n -= 1
    
