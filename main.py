class Knight:
    def __init__(self, horizontal, vertical, color, alf='abcdefgh'):
        self.horizontal = horizontal
        self.vertical = vertical
        self.color = color
        self.index = alf.find(horizontal) + 1

    def get_char(self):
        return 'N'

    def can_move(self, x, y):
        xx = 'abcdefgh'.find(x) + 1
        f1 = abs(xx - self.index) == 2 and abs(y - self.vertical) == 1
        f2 = abs(xx - self.index) == 1 and abs(y - self.vertical) == 2
        f3 = (1 <= xx <= 8 and 1 <= y <= 8)
        if (f1 or f2) and f3:
            return True
        return False

    def move_to(self, x, y):
        if self.can_move(x, y):
            self.horizontal = x
            self.vertical = y

    def draw_board(self):
        for i in range(1, 9):
            for j in range(1, 9):
                ii = -i % 9
                if self.can_move('abcdefgh'[ii-1], j):
                    print('*', end='')
                elif ii == self.index and j == self.vertical:
                    print('N', end='')
                else:
                    print('.', end='')
            print()