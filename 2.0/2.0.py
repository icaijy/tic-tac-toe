# set default
demoBoard = '''
----------------
| １ | ２ | ３ |
----------------
| ４ | ５ | ６ |
----------------
| ７ | ８ | ９ |
----------------
'''
cbn = {
    1:(0,0),
    2:(0,1),
    3:(0,2),
    4:(1,0),
    5:(1,1),
    6:(1,2),
    7:(2,0),
    8:(2,1),
    9:(2,2)
}
piece = {
    0:'　',  # O:ai X:player
    1:'Ｏ',
    2:'Ｘ',
}
# end


def MCB(CB):
    a = piece[CB[0][0]]
    b = piece[CB[0][1]]
    c = piece[CB[0][2]]
    d = piece[CB[1][0]]
    e = piece[CB[1][1]]
    f = piece[CB[1][2]]
    g = piece[CB[2][0]]
    h = piece[CB[2][1]]
    i = piece[CB[2][2]]

    checkerboard = 16*'-'+'\n| '+ a +' | ' + b +' | ' + c +' |\n'+ \
                   16 * '-' + '\n| ' + d + ' | ' + e + ' | ' + f + ' |\n'+\
    16 * '-' + '\n| ' + g + ' | ' + h + ' | ' + i + ' |\n'+16*'-'

    return checkerboard

# end


def ai():
    global checkerboard

    # the middle of checkerboard, it's a good place
    if checkerboard[1][1]==0:
        checkerboard[1][1] = 1
        return
    # end
    def col(col, PorAI):
        if checkerboard[col].count(PorAI) == 2 and checkerboard[col].count(0)==1:
            checkerboard[col][checkerboard[col].index(0)] = 1
            return True

    def row(row, PorAI):
        rows = [checkerboard[0][row], checkerboard[1][row], checkerboard[2][row]]
        if rows.count(PorAI) == 2 and rows.count(0) == 1:
            checkerboard[rows.index(0)][row] = 1
            return True

    def oblique(a, b, PorAI):
        oblique = [checkerboard[0][a], checkerboard[1][1], checkerboard[2][b]]
        q = {
            0:a,
            1:1,
            2:b
        }
        if oblique.count(PorAI) == 2 and oblique.count(0) == 1:
            zero = oblique.index(0)
            checkerboard[zero][q[zero]] = 1
            return True

    def ran():
        for x in range(0,3):
            if checkerboard[x].count(0)!=0:
                checkerboard[x][checkerboard[x].index(0)] = 1
                return
    for y in [1,2]:
        for x in range(0,3):
            if col(x,y):
                return
    for y in [1,2]:
        for x in range(0,3):
            if row(x,y):
                return
    for x in [1,2]:
        if oblique(0,2,x):
            return
        if oblique(2,0,x):
            return
    ran()


def player():
    global checkerboard
    while True:     # Fuck!I don't like stack overflow!
        try:
            choose = int(input('Please type where do you want to choose: '))
        except:
            print('Please type number.')
            continue

        # judge is it in the range
        if choose not in range(1,10):
            print('Opps!Please choose again,the range is 1~9.')
            continue

        while True:
            t = cbn[choose][0]
            r = cbn[choose][1]
            if checkerboard[t][r]!=0:
                print('Sorry,this had been choosing,please change one.')
                break
                #choose = int(input('Please type where do you want to choose: '))
            else:
                #break
                checkerboard[t][r] = 2
                return

def juperWinlose():
    global checkerboard
    def col(col, PorAI):
        if checkerboard[col].count(PorAI) == 3:
            return PorAI


    def row(row, PorAI):
        rows = [checkerboard[0][row], checkerboard[1][row], checkerboard[2][row]]
        if rows.count(PorAI) == 3:
            return PorAI

    def oblique(a, b, PorAI):
        oblique = [checkerboard[0][a], checkerboard[1][1], checkerboard[2][b]]
        if oblique.count(PorAI) == 3:
            return PorAI


    for y in [1, 2]:
        for x in range(0, 3):
            if col(x, y)!=None:
                return col(x, y)
    for y in [1, 2]:
        for x in range(0, 3):
            if row(x, y)!=None:
                return row(x, y)
    for x in [1, 2]:
        if oblique(0, 2, x)!=None:
            return oblique(0, 2, x)
        if oblique(2, 0, x)!=None:
            return oblique(2, 0, x)
    if  checkerboard[0].count(0)==0 and checkerboard[1].count(0)==0 and checkerboard[2].count(0)==0:
        return 3
    return None
def handle_winLose(w):
    if w == 1:
        a = input('Computer win!try again next time!Press enter to exit, type any thing play again!')
        if a == '':
            exit()
        else:
            start()
    if w == 2:
        a = input('You win!!!Press enter to exit, type any thing play again!')
        if a == '':
            exit()
        else:
            start()
    if w == 3:
        a = input('Draw!Press enter to exit, type any thing play again!')
        if a == '':
            exit()
        else:
            start()
    if w==None:
        return

def AiFirst():
    print('Computer first!')
    print(demoBoard)
    print("Then, use this number, to choose, let's start!")
    while True:
        ai()
        print(MCB(checkerboard))
        handle_winLose(juperWinlose())
        player()
        handle_winLose(juperWinlose())


def PlayerFirst():
    print('You first!')
    print(demoBoard)
    print("Then, use this number, to choose, let's start!")
    while True:
        player()
        handle_winLose(juperWinlose())
        ai()
        print(MCB(checkerboard))
        handle_winLose(juperWinlose())

def start():
    global checkerboard
    checkerboard = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]   # write here because if player want to play again, you should init the checkerboard.
    while True:
        text = '''
Please choose mode:
1:computer first
2:you first
3:random: '''
        mode = int(input(text))
        if mode != None:
            break
        else:
            print('Opps!Choose error, please choose again!')

    if mode == 3:
        import random
        mode = random.choice([2, 1])
    if mode == 1:
        AiFirst()
    if mode == 2:
        PlayerFirst()

if __name__ == '__main__':
    start()

