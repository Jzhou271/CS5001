
import math
import copy


def choice():
    while True:
        choice = input("Create your own maze or Read a file? \n"
                       "Enter C to create your own maze \n"
                       "Enter F to read a file \n"
                       "Enter Q to quit \n"
                       "Please enter here(C/F/Q): ")
        if choice == "C":
            maze = read_maze_from_keyboard()
            return maze
        elif choice == "F":
            maze = read_maze_from_file()
            return maze
        elif choice == "Q":
            return None
        else:
            print("Wrong opition is chosen, please enter C/F/Q again")



def read_maze_from_keyboard():
    try:
        width = int(input("Enter width: "))
        height = int(input("Enter height: "))
    except ValueError:
        print("Please enter integers")
    if width < 3 or width > 120:
        print("width must be greater and equal to 3 and"
              "smaller and equal to 120")
        return
    if height < 3 or height > 40:
        print("height must be greater and equal to 3 and"
              "smaller and equal to 40")
        return

    maze = [[width, height]]
    for i in range(height):
        line_of_maze = input("Enter line by line of the maze: \n")
        while len(line_of_maze) != width:
            print("Incorrect width range!")
            line_of_maze = input("Re-enter this line of maze: \n")
        maze.append(line_of_maze)

    if not check_maze(maze):
        quit()

    for character in maze[1:]:
        print(character)
    return maze


def read_maze_from_file():
    filename = input("Enter file name: ")
    try:
        input_file = open(filename, 'r')
    except FileNotFoundError:
        print(filename, "does not exist")
        return
    except PermissionError:
        print("Filename", filename, "\n"
              "You do not have sufficient permissions to open", filename)
        return
    except OSError:
        print("Filename", filename, "\n"
              "An unexpected error occurred while attempting to open",
              filename)
        return
    input_file.readline()
    file_data = input_file.readlines()
    input_file.close()

    maze = []
    for i in (file_data):
        i = i.strip()
        maze.append(i)
    if len(maze) == 0:
        print("This file is an empty file")
        quit()

    width = len(maze[0])
    height = len(maze)

    if width < 3 or width > 120:
        print("width must be greater and equal to 3 and"
              "smaller and equal to 120")
        return
    if height < 3 or height > 40:
        print("height must be greater and equal to 3 and"
              "smaller and equal to 40")
        return

    if not check_maze(maze):
        quit()

    for character in maze:
        print(character)
    return maze


def check_maze(maze):
    check_maze = set()
    for i in maze[1:]:
        for j in i:
            if j == 'X' or j == 'E' or j == ' ':
                check_maze.add(j)
            else:
                print("The maze has incorrect input character")
                return False

    if 'E' not in check_maze:
        print("The maze does not have an exist")
        return False

    if 'X' not in check_maze:
        print("The maze does not have a wall")
        return False

    if ' ' not in check_maze:
        print("The maze does not have a open space for player")
        return False

    for i in maze[0] and maze[-1]:
        if i != 'X' and i != 'E':
            print("The top and the bottom wall has incorrect input character")
            return False
        else:
            continue
    for i in maze:
        if i[0] and i[-1] == 'X' or i[0] and i[-1] == 'E':
            continue
    return True


def get_neighbors(point):
    x = point[0]
    y = point[1]
    return [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]


direction = {}
def find_exits(maze, start):
   # initialization
   distance = {}
   width = len(maze)
   height = len(maze[0])
   for i in range(width):
       for j in range(height):
           distance[(i, j)] = float('inf')
           direction[(i, j)] = None


   # calculating the quickest way out of the maze
   worklist = [start]
   distance[start] = 0
   while len(worklist) > 0:
      current = worklist[0]
      neighbors = get_neighbors(current)
      for i in range(len(neighbors)):
          neighbor = neighbors[i]
          x = neighbor[0]
          y = neighbor[1]
          if x >= 0 and x < width and y >= 0 and y < height \
             and math.isinf(distance[neighbor]) \
             and (maze[x][y] == ' ' or maze[x][y] == 'E'):
              distance[neighbor] = distance[current] + 1
              direction[neighbor] = i
              worklist.append(neighbor)
      worklist.remove(current)

def get_next_location(current, direction_int):
    if direction_int == 0:
        return (current[0] - 1, current[1])
    elif direction_int == 1:
        return (current[0], current[1] - 1)
    elif direction_int == 2:
        return (current[0] + 1, current[1])
    else:
        return (current[0], current[1] + 1)


def get_path_to_exit(maze, start, exit):
   final_path = []
   current = exit
   while current in direction.keys() and direction[current] is not None:
       next_location = get_next_location(current, direction[current])
       final_path.append(current)
       current = next_location
   final_path.append(start)
   return final_path


def start_location(maze):
    width = len(maze)
    height = len(maze[0])
    try:
        start_x = int(input("Please enter your x coordinate: "))
        start_y = int(input("Please enter your y coordinate: "))
    except ValueError:
        print("Please enter integers")
    if start_x < 0 or start_x > width:
        print("Input x coordinate is out of bonds")
    if start_y < 0 or start_y > height:
        print("Input y coordinate is out of bonds")
    if maze[start_x][start_y] != " ":
        print("Coordinate: ", start_x, start_y,
              "is occupied, please re-enter a location.\n")
    return start_x, start_y


def footprint(maze):
    start = start_location(maze)
    exit_pos = []
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'E':
                exit_pos.append((i, j))
    for pos in exit_pos:
        maze_store = copy.deepcopy(maze)
        set_other_to_blank(maze, pos[0], pos[1])
        find_exits(maze, start)
        ret = get_path_to_exit(maze, start, pos)
        print()
        for (i, j) in ret:
            maze[i] = maze[i][0:j] + '*' + maze[i][j + 1:]
        (i, j) = start
        maze[i] = maze[i][0:j] + 'S' + maze[i][j + 1:]
        (i, j) = pos
        maze[i] = maze[i][0:j] + 'E' + maze[i][j + 1:]
        if len(ret) > 2:
            for character in maze:
                print(character)
            print("The maze needs", len(ret) - 2, "steps to find the exit")
        else:
            print('No way out')
        print()
        maze = maze_store


def set_other_to_blank(maze, x, y):
    width = len(maze)
    height = len(maze[0])
    for i in range(width):
        for j in range(height):
            if (i, j) != (x, y) and maze[i][j] == 'E':
                maze[i] = maze[i][0:j] + ' ' + maze[i][j + 1:]


def main():
    maze = choice()
    if maze is None:
        return
    footprint(maze)
    

if __name__ == '__main__':
    main()
