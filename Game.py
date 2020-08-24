class Game:
    def __init__(self):
        self.state = []
        self.occupied = False
        for i in range(9):
            self.state.append(None)

    def move(self, field, symbol):
        self.occupied = False
        if self.state[field] is None:
            self.state[field] = symbol
        else:
            self.occupied = True

    @property
    def get_occ(self):
        return self.occupied

    def win_check(self):
        if self.state[0] == self.state[1] == self.state[2]:
            return self.state[0]
        elif self.state[3] == self.state[4] == self.state[5]:
            return self.state[3]
        elif self.state[6] == self.state[7] == self.state[8]:
            return self.state[6]
        elif self.state[0] == self.state[3] == self.state[6]:
            return self.state[6]
        elif self.state[1] == self.state[4] == self.state[7]:
            return self.state[1]
        elif self.state[2] == self.state[5] == self.state[8]:
            return self.state[2]
        elif self.state[0] == self.state[4] == self.state[8]:
            return self.state[0]
        elif self.state[2] == self.state[4] == self.state[6]:
            return self.state[2]
        else:
            return False
