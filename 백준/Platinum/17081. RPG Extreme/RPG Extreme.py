from collections import deque


class User:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.max_hp = 20
        self.cur_hp = 20
        self.power = 2
        self.body = 2
        self.exp = 0
        self.level = 1
        self.weapon = 0
        self.armor = 0
        # HR | RE | CO | EX | DX | HU | CU
        self.accessories = [0] * 7
        self.atk_buf = 1

    def get_exp(self, exp):
        if self.accessories[EX]:
            exp = int(1.2 * exp)
        self.exp += exp
        if self.exp >= 5 * self.level:
            self.exp = 0
            self.max_hp += 5
            self.cur_hp = self.max_hp
            self.power += 2
            self.body += 2
            self.level += 1

    def get_damage(self, damage):
        global game_over
        self.cur_hp -= damage
        if self.cur_hp <= 0:
            self.cur_hp = 0

    def get_heal(self, heal):
        self.cur_hp += heal
        if self.cur_hp > self.max_hp:
            self.cur_hp = self.max_hp

    def get_atk(self):
        return self.power + self.weapon

    def get_def(self):
        return self.body + self.armor

    def die(self):
        global game_over
        game_over = True
        self.row = -1
        self.col = -1

    def resurrect(self):
        self.cur_hp = self.max_hp
        self.row, self.col = init_position
        self.accessories[1] = 0

    def move(self, direction):
        dest_row = self.row + DIRECTIONS[direction][0]
        dest_col = self.col + DIRECTIONS[direction][1]
        if 0 <= dest_row < height and 0 <= dest_col < width and grid[dest_row][dest_col] != '#':
            self.row = dest_row
            self.col = dest_col

    def fight(self, mob):
        global game_clear
        # First attack for each side
        shield = False
        if self.accessories[HU] and isinstance(mob, Boss):
            self.cur_hp = self.max_hp
            shield = True
        if self.accessories[CO]:
            if self.accessories[DX]:
                first_attack = max(1, 3 * self.get_atk() - mob.body)
            else:
                first_attack = max(1, 2 * self.get_atk() - mob.body)
        else:
            first_attack = max(1, self.get_atk() - mob.body)
        mob.cur_hp -= first_attack
        if mob.cur_hp <= 0:
            if isinstance(mob, Boss):
                game_clear = True
            return True
        if not shield:
            self.get_damage(max(1, mob.power - self.get_def()))
            if self.cur_hp <= 0:
                if self.accessories[RE]:
                    self.resurrect()
                    mob.cur_hp = mob.max_hp
                    return None
                else:
                    self.die()
                    return False

        # After first attack
        while True:
            mob.cur_hp -= max(1, self.get_atk() - mob.body)
            if mob.cur_hp <= 0:
                if isinstance(mob, Boss):
                    game_clear = True
                return True
            self.get_damage(max(1, mob.power - self.get_def()))
            if self.cur_hp <= 0:
                if self.accessories[RE]:
                    self.resurrect()
                    mob.cur_hp = mob.max_hp
                    return None
                else:
                    self.die()
                    return False


    def get_item(self, item):
        grid[self.row][self.col] = None
        if item.item_type == 'W':
            self.weapon = int(item.value)
        elif item.item_type == 'A':
            self.armor = int(item.value)
        elif not self.accessories[ITEM_DICT[item.value]] and sum(self.accessories) < 4:
            self.accessories[ITEM_DICT[item.value]] = 1

    def interaction(self):
        cur_situation = grid[self.row][self.col]
        if cur_situation is None:
            pass
        elif cur_situation == '^':
            if self.accessories[DX]:
                self.get_damage(1)
            else:
                self.get_damage(5)
            if self.cur_hp <= 0:
                if self.accessories[RE]:
                    self.resurrect()
                else:
                    self.die()
        elif isinstance(cur_situation, Mob):
            won = self.fight(cur_situation)
            if won is None:
                pass
            elif not won:
                user_killer.name = cur_situation.name
            else:
                grid[self.row][self.col] = None
                self.get_exp(cur_situation.exp)
                if self.accessories[HR]:
                    self.get_heal(3)
        elif isinstance(cur_situation, Item):
            self.get_item(cur_situation)

    def __repr__(self):
        return f"{self.row} {self.col}"

    def prt_info(self):
        print(f'''LV : {self.level}
HP : {self.cur_hp}/{self.max_hp}
ATT : {self.power}+{self.weapon}
DEF : {self.body}+{self.armor}
EXP : {self.exp}/{self.level * 5}''')


class Mob:
    def __init__(self, row, col, name, power, body, max_hp, exp):
        self.row = row
        self.col = col
        self.name = name
        self.power = power
        self.body = body
        self.max_hp = max_hp
        self.cur_hp = max_hp
        self.exp = exp

    def __repr__(self):
        return '&'

class Boss(Mob):
    def __repr__(self):
        return 'M'


class Item:
    def __init__(self, item_type, value):
        self.item_type = item_type
        self.value = value

    def __repr__(self):
        return 'B'


def prt_result():
    for r in range(height):
        for c in range(width):
            if user.row == r and user.col == c:
                print('@', end='')
            elif grid[r][c] is None:
                print('.', end='')
            else:
                print(grid[r][c], end='')
        print()
    print("Passed Turns :", command_cnt - len(commands))
    user.prt_info()
    if game_clear:
        print("YOU WIN!")
    elif game_over:
        print(f"YOU HAVE BEEN KILLED BY {user_killer.name}..")
    else:
        print("Press any key to continue.")


DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
HR, RE, CO, EX, DX, HU, CU = 0, 1, 2, 3, 4, 5, 6
ITEM_DICT = {"HR":0, "RE":1, "CO":2, "EX":3, "DX":4, "HU":5, "CU":6}

height, width = map(int, input().split())
board = [list(input()) for _ in range(height)]
grid = [[None] * width for _ in range(height)]
mob_cnt = 0
item_cnt = 0
user = User(-1, -1)
for r in range(height):
    for c in range(width):
        if board[r][c] in '&M':
            mob_cnt += 1
        elif board[r][c] == 'B':
            item_cnt += 1
        elif board[r][c] == '@':
            user = User(r, c)
            init_position = r, c
        elif board[r][c] == '^':
            grid[r][c] = '^'
        elif board[r][c] == '#':
            grid[r][c] = '#'

commands = deque(list(input()))
command_cnt = len(commands)

for _ in range(mob_cnt):
    ipt = list(input().split())
    r = int(ipt[0]) - 1
    c = int(ipt[1]) - 1
    if board[r][c] == '&':
        mob = Mob(r, c, ipt[2], int(ipt[3]), int(ipt[4]), int(ipt[5]), int(ipt[6]))
    else:
        mob = Boss(r, c, ipt[2], int(ipt[3]), int(ipt[4]), int(ipt[5]), int(ipt[6]))
    grid[int(ipt[0]) - 1][int(ipt[1]) - 1] = mob

for _ in range(item_cnt):
    ipt = list(input().split())
    item = Item(ipt[2], ipt[3])
    grid[int(ipt[0]) - 1][int(ipt[1]) - 1] = item

game_over = False
game_clear = False
user_killer = Mob(-1, -1, "SPIKE TRAP", -1, -1, -1, -1)
while commands and not game_over and not game_clear:
    command = commands.popleft()
    if command == 'L':
        user.move(2)
    elif command == 'R':
        user.move(0)
    elif command == 'U':
        user.move(3)
    else:
        user.move(1)
    user.interaction()

prt_result()
