
i = 1
dot_count = 3 - 1

vertical_bar = "|"
slash = "/"
backslash = "\\"
dot = "."

while i < 4:
    print(vertical_bar + dot * dot_count + (slash + backslash) * i +
          2 * dot * dot_count + (slash + backslash) * i + dot * dot_count
          + vertical_bar)
    i += 1
    dot_count -= 1
