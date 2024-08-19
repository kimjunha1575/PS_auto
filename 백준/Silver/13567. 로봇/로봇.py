
M, n = map(int, input().split())
commands = []
for _ in range(n):
    command, param = input().split()
    if command == "TURN":
        commands.append((0, int(param)))
    else:
        commands.append((1, int(param)))
valid_command_set = True
x = 0
y = 0
direction = 0
dirs = ((0, 1), (-1, 0), (0, -1), (1, 0))
for command, param in commands:
    if command:
        y += param * dirs[direction][0]
        x += param * dirs[direction][1]
    elif param == 1:
        direction = (direction + 1) % 4
    else:
        direction = (direction - 1) % 4
    if not (0 <= x < M and 0 <= y < M):
        valid_command_set = False
        break

if valid_command_set:
    print(x, y)
else:
    print(-1)
