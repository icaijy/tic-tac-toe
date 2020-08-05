# what's new
1. Fix some bugs.
2. Change some English words.
3. code refactoring, once and only once.
4. Optimize user experience:
- new **choose mode**(player first, AI first and random), 
- new **game loop**, user can **choose exit or continue**.
5. Make the AI *smarter*.
# what should I improvement?
1. make the AI smarter
2. make the GUI, there is two ways:
- use turtle
- use frame,for example:django, Flask
3. save user record: user name
4. save game records: date, result....
# game demo:
```
Please choose mode:
1:computer first
2:you first
3:random: 3
You first!

----------------
| １ | ２ | ３ |
----------------
| ４ | ５ | ６ |
----------------
| ７ | ８ | ９ |
----------------

Then, use this number, to choose, let's start!
Please type where do you want to choose: 5
----------------
| Ｏ | 　 | 　 |
----------------
| 　 | Ｘ | 　 |
----------------
| 　 | 　 | 　 |
----------------
Please type where do you want to choose: 1
Sorry,this had been choosing,please change one.
Please type where do you want to choose: 11
Opps!Please choose again,the range is 1~9.
Please type where do you want to choose: 2
----------------
| Ｏ | Ｘ | 　 |
----------------
| 　 | Ｘ | 　 |
----------------
| 　 | Ｏ | 　 |
----------------
Please type where do you want to choose: 3
----------------
| Ｏ | Ｘ | Ｘ |
----------------
| 　 | Ｘ | 　 |
----------------
| Ｏ | Ｏ | 　 |
----------------
Please type where do you want to choose: 4
----------------
| Ｏ | Ｘ | Ｘ |
----------------
| Ｘ | Ｘ | 　 |
----------------
| Ｏ | Ｏ | Ｏ |
----------------
Computer win!try again next time!Press enter to exit, type any thing play again!

tictactoe>
```
