# import module and set unchanged variable.
other_function = __import__('other_function')
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

checkerboard = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
]
# mode = other_function.chooseMode()
# other_function.judge_input(mode)
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
# print(demoBoard)
# print(MCB(checkerboard))

def ai():
    global checkerboard
    if checkerboard[1][1]==0:
        checkerboard[1][1] = 1
        return None

    # cal
    try:
        if checkerboard[0].count(2) == 2 and checkerboard.count(1)!=1:
            checkerboard[0][checkerboard[0].index(0)] = 1
            return  None
    except:
        pass
    try:
        if checkerboard[1].count(2) == 2 and checkerboard.count(1)!=1:
            checkerboard[1][checkerboard[1].index(0)] = 1
            return  None
    except:
        pass
    try:
        if checkerboard[2].count(2) == 2 and checkerboard.count(1)!=1:
            checkerboard[2][checkerboard[2].index(0)] = 1
            return  None
    except:
        pass
    # end


    # row
    try:
        # print(checkerboard[0][0])
        # print(checkerboard[1][0])
        # print(checkerboard[2][0])
        row = [checkerboard[0][0], checkerboard[1][0], checkerboard[2][0]]
        if row.count(2)==2 and row.count(1)!=1:
            NI = row.index(0)
            if NI==0:
                checkerboard[0][0] = 1
                return
            elif NI == 1:
                checkerboard[1][0] = 1
                return
            else:
                checkerboard[2][0] = 1
                return
    except:
        pass

    try:
        row = [checkerboard[0][1], checkerboard[1][1], checkerboard[2][1]]
        if row.count(2)==2 and row.count(1)!=1:
            NI = row.index(0)
            if NI==0:
                checkerboard[0][1] = 1
                return
            elif NI == 1:
                checkerboard[1][1] = 1
                return
            else:
                checkerboard[2][1] = 1
                return
    except:
        pass
    row = [checkerboard[0][2], checkerboard[1][2], checkerboard[2][2]]
    try:
        if row.count(2)==2 and row.count(1)!=1:
            NI = row.index(0)
            if NI==0:
                checkerboard[0][2] = 1
                return
            elif NI == 1:
                checkerboard[1][2] = 1
                return
            else:
                checkerboard[2][2] = 1
                return
    except:
        pass
    del row
    # oblique
    try:
        oblique = [checkerboard[0][0], checkerboard[1][1], checkerboard[2][2]]
        if oblique.count(2)==2 and oblique.count(1)!=1:
            NI = oblique.index(0)
            if NI==0:
                checkerboard[0][0] = 1
                return
            elif NI == 1:
                checkerboard[1][1] = 1
                return
            else:
                checkerboard[2][2] = 1
                return
    except:
        pass

    try:
        oblique = [checkerboard[0][2], checkerboard[1][1], checkerboard[2][0]]
        if oblique.count(2)==2 and oblique.count(1)!=1:
            NI = oblique.index(0)
            if NI==0:
                checkerboard[0][2] = 1
                return
            elif NI == 1:
                checkerboard[1][1] = 1
                return
            else:
                checkerboard[2][0] = 1
                return
    except:
        pass
    del oblique
    # end
    # else
    try:
        Noneindex = checkerboard[0].index(0)
        checkerboard[0][Noneindex] = 1
        return
    except:
        try:
            Noneindex = checkerboard[1].index(0)
            checkerboard[1][Noneindex] = 1
            return
        except:
            Noneindex = checkerboard[0].index(0)
            checkerboard[2][Noneindex] = 1
            return


def player():
    global checkerboard
    while True:     # Fuck!I don't like stack overflow!
        try:
            choose = int(input('Please type where do you want to choose.'))
        except:
            print('Please type number.')
            continue
        # judge is it in the range
        if choose not in range(1,10):
            print('Opps!Please choose again,the range is 1~9.')
        else:
            break
    while True:
        t = cbn[choose][0]
        r = cbn[choose][1]
        if checkerboard[t][r]!=0:
            print('Sorry,this had been choose,please change one.')
            choose = int(input('Please type where do you want to choose.'))
        else:
            break
    checkerboard[t][r] = 2
    return

def juperWinlose():
    global checkerboard
    if checkerboard[0].count(2) == 3:
        print('You win!!!')
        input("type any things to exit")()
        exit()
    if checkerboard[1].count(2) == 3:
        print('You win!!!')
        input("type any things to exit")()
        exit()
    if checkerboard[1].count(2) == 3:
        print('You win!!!')
        input("type any things to exit")()
        exit()
    if checkerboard[0].count(1) == 3:
        print('Computer win,Try again next time!')
        input("type any things to exit")()
        exit()
    if checkerboard[1].count(1) == 3:
        print('Computer win,Try again next time!')
        input("type any things to exit")
        exit()
    if checkerboard[2].count(1) == 3:
        print('Computer win,Try again next time!')
        input("type any things to exit")
        exit()

    row = [checkerboard[0][0],checkerboard[1][0],checkerboard[2][0]]
    if row.count(2)==3:
        print('You win!!!')
        input("type any things to exit")
        exit()
    row = [checkerboard[0][1], checkerboard[1][1], checkerboard[2][1]]
    if row.count(2)==3:
        print('You win!!!')
        input("type any things to exit")
        exit()
    row = [checkerboard[0][2], checkerboard[1][2], checkerboard[2][2]]
    if row.count(2)==3:
        print('You win!!!')
        input("type any things to exit")
        exit()
    row = [checkerboard[0][0],checkerboard[1][0],checkerboard[2][0]]
    if row.count(1)==3:
        print('Computer win,Try again next time!')
        input("type any things to exit")
        exit()
    row = [checkerboard[0][1], checkerboard[1][1], checkerboard[2][1]]
    if row.count(1)==3:
        print('Computer win,Try again next time!')
        input("type any things to exit")
        exit()
    row = [checkerboard[0][2], checkerboard[1][2], checkerboard[2][2]]
    if row.count(1)==3:
        print('Computer win,Try again next time!')
        input("type any things to exit")
        exit()

    # oblique
    oblique = [checkerboard[0][0],checkerboard[1][1],checkerboard[2][2]]
    if oblique.count(2)==3:
        print('You win!!!')
        input("type any things to exit")
        exit()
    oblique = [checkerboard[0][2], checkerboard[1][1], checkerboard[2][0]]
    if oblique.count(2) == 3:
        print('You win!!!')
        input("type any things to exit")
        exit()
    oblique = [checkerboard[0][0], checkerboard[1][1], checkerboard[2][2]]
    if oblique.count(1) == 3:
        print('Computer win,Try again next time!')
        input("type any things to exit")
        exit()
    oblique = [checkerboard[0][2], checkerboard[1][1], checkerboard[2][0]]
    if oblique.count(1) == 3:
        print('Computer win,Try again next time!')
        input("type any things to exit")
        exit()
    if 0 not in checkerboard[0] and 0 not in checkerboard[1] and 0 not in checkerboard[2]:
        print('draw!!')
        input("type any things to exit")
        exit()
    else:
        return

if __name__ == '__main__':
    print(demoBoard)
    input("Than, use this number, to choose, press enter to start!")
    while True:
        #print(checkerboard)
        ai()
        print(MCB(checkerboard))
        juperWinlose()
        player()
        juperWinlose()

# --------------
# | Ｏ | Ｏ | ３ |
# --------------
# | ４ | Ｏ | ６ |
# --------------
# | Ｘ | Ｘ | Ｏ |
# --------------

