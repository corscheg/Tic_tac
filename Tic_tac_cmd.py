from Game import Game

m = Game()

print('Hello!\nWelcome to tic-tac toe!\nYou see a playing fields. Every turn you should type a digit matching to field you want to insert a symbol.')
print('_____________')
print('| 7 | 8 | 9 |')
print('|---|---|---|')
print('| 4 | 5 | 6 |')
print('|---|---|---|')
print('| 1 | 2 | 3 |')
print('-------------')


while not m.win_check():
    field = int(input(m.get_player + ' turn:'))
    m.move(field - 1)

print('%s won!' % m.win_check())
