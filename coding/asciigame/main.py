sprite = "|/|"
x_position = 0  # Horizontal position (left to right)
y_position = 0  # Vertical position (up and down)
max_x = 20  # Max horizontal positions (width)
max_y = 5  # Max vertical positions (height)

# Create a grid of empty spaces
grid = [[" " for _ in range(max_x)] for _ in range(max_y)]

while True:
    move = input("Enter your direction (wasd, exit): ")

    # Clear the current sprite position by replacing it with a blank space
    grid[y_position][x_position] = " "

    # Move the sprite based on the user input
    if move == "s" and y_position < max_y - 1:
        y_position += 1
    elif move == "w" and y_position > 0:
        y_position -= 1
    elif move == "a" and x_position > 0:
        x_position -= 1
    elif move == "d" and x_position < max_x - 1:
        x_position += 1
    elif move == "exit":
        break

    # Place the sprite at the new position
    grid[y_position][x_position] = sprite

    # Clear the screen and print the grid
    print("\033c", end="")  # This is an ANSI escape code to clear the terminal
    for row in grid:
        print("".join(row))

