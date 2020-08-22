class Game:
    def __init__(self):
        self.state = []
        for i in range(9):
            self.state.append(None)

    def move(self, field, symbol):
        self.state[field] = symbol

    def win_check(self):
        if self.state[1] == self.state[2] == self.state[3]:
            return self.state[1]
        elif self.state[4] == self.state[5] == self.state[6]:
            return self.state[4]
        elif self.state[7] == self.state[8] == self.state[9]:
            return self.state[7]
        elif self.state[1] == self.state[4] == self.state[7]:
            return self.state[7]
        elif self.state[2] == self.state[5] == self.state[8]:
            return self.state[2]
        elif self.state[3] == self.state[6] == self.state[9]:
            return self.state[3]
        elif self.state[1] == self.state[5] == self.state[9]:
            return self.state[1]
        elif self.state[3] == self.state[5] == self.state[7]:
            return self.state[3]
        else:
            return False
