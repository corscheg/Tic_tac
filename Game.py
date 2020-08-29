class Game:
    def __init__(self):
        self.state = []
        self.player = '0'
        self.win_line = []
        for i in range(9):
            self.state.append(None)

    def move(self, field):
        if self.state[field] is None:
            self.state[field] = self.player
            if self.player == '0':
                self.player = 'X'
            else:
                self.player = '0'

    def get_occ(self, field):
        if self.state[field] is None:
            return False
        else:
            return True

    @property
    def get_player(self):
        return self.player

    @property
    def get_win_line(self):
        return self.win_line

    def win_check(self):
        if (self.state[0] == self.state[1] == self.state[2]) and (self.state[0] is not None):
            self.win_line = [0, 2]
            return self.state[0]
        elif (self.state[3] == self.state[4] == self.state[5]) and (self.state[3] is not None):
            self.win_line = [3, 5]
            return self.state[3]
        elif (self.state[6] == self.state[7] == self.state[8]) and (self.state[6] is not None):
            self.win_line = [6, 8]
            return self.state[6]
        elif (self.state[0] == self.state[3] == self.state[6]) and (self.state[0] is not None):
            self.win_line = [0, 6]
            return self.state[6]
        elif (self.state[1] == self.state[4] == self.state[7]) and (self.state[1] is not None):
            self.win_line = [1, 7]
            return self.state[1]
        elif (self.state[2] == self.state[5] == self.state[8]) and (self.state[2] is not None):
            self.win_line = [2, 8]
            return self.state[2]
        elif (self.state[0] == self.state[4] == self.state[8]) and (self.state[0] is not None):
            self.win_line = [0, 8]
            return self.state[0]
        elif (self.state[2] == self.state[4] == self.state[6]) and (self.state[2] is not None):
            self.win_line = [2, 6]
            return self.state[2]
        else:
            s = 0
            for i in self.state:
                if i is not None:
                    s += 1
            if s != 9:
                return False
            else:
                return 'Draw'
