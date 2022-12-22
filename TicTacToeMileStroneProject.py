playerParameters=[0,1,2,3,4,5,6,7,8]
boardDimentions=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
boardParameters=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
def board():
    print(boardParameters[6]+boardDimentions[6]+'|'+boardParameters[7]+boardDimentions[7]+'|'+boardParameters[8]+boardDimentions[8])
    print('--------')
    print(boardParameters[3]+boardDimentions[3]+'|'+boardParameters[4]+boardDimentions[4]+'|'+boardParameters[5]+boardDimentions[5])
    print('--------')
    print(boardParameters[0]+boardDimentions[0]+'|'+boardParameters[1]+boardDimentions[1]+'|'+boardParameters[2]+boardDimentions[2])
    return ""

def assigning_players_characters():
    player2='O'
    characterAssigning=0
    while characterAssigning==0:
        player1=input("Please cloose your character (X or O): ")
        if player1=='X':
            characterAssigning=1
        elif player1=='O':
            player2='X'
            characterAssigning=1
        else:
            print("The character was not recognized please make sure you choose the correct character.")
            characterAssigning=0
        if player1=='X' or player1=='O':
            print(f"Player 1 has chosen {player1}")
            print(f"Player 2 has chosen {player2}")
        else:
            pass
        return player1, player2

def gameplay1(sign1,sign2):
    player1Input=0
    gameOver=0
    player1Input=int(input("Please Enter your Input (player 1): "))
    boardParameters[player1Input]= sign1
    print(board())
    if boardParameters[0]==sign1:
        if boardParameters[1]==sign1 and boardParameters[2]==sign1:
            gameOver+=1
        elif boardParameters[3]==sign1 and boardParameters[6]==sign1:
            gameOver+=1
        elif boardParameters[4]==sign1 and boardParameters[8]==sign1:
            gameOver+=1
    elif boardParameters[3]==sign1:
        if boardParameters[4]==sign1 and boardParameters[5]==sign1:
            gameOver+=1
    elif boardParameters[6]==sign1:
        if boardParameters[7]==sign1 and boardParameters[8]==sign1:
            gameOver+=1
        elif boardParameters[4]==sign1 and boardParameters[2]==sign1:
            gameOver+=1    
    elif boardParameters[1]==sign1:
        if boardParameters[4]==sign1 and boardParameters[7]==sign1: 
            gameOver+=1
    elif boardParameters[2]==sign1:
        if boardParameters[5]==sign1 and boardParameters[8]==sign1:
            gameOver+=1
        elif boardParameters[4]==sign1 and boardParameters[6]==sign1:
            gameOver+=1
    if(gameOver==1):
        print("Player 1 Wins")
    if(gameOver==0):
        gameOver=gameplay2(sign2)
    return gameOver

def gameplay2(sign2):
    player2Input=0
    gameOver=0
    player2Input=int(input("Please Enter your Input (Player 2): "))
#     if player1Input and player2Input in playerParameters:
    boardParameters[player2Input]= sign2
    print(board())
    if boardParameters[0]==sign2:
        if boardParameters[1]==sign2 and boardParameters[2]==sign2:
            gameOver+=1
        elif boardParameters[3]==sign2 and boardParameters[6]==sign2:
            gameOver+=1
        elif boardParameters[4]==sign2 and boardParameters[8]==sign2:
            gameOver+=1
    elif boardParameters[3]==sign2:
        if boardParameters[4]==sign2 and boardParameters[5]==sign2:
            gameOver+=1
    elif boardParameters[6]==sign2:
        if boardParameters[7]==sign2 and boardParameters[8]==sign2:
            gameOver+=1
    elif boardParameters[1]==sign2:
        if boardParameters[4]==sign2 and boardParameters[7]==sign2: 
            gameOver+=1
    elif boardParameters[2]==sign2:
        if boardParameters[5]==sign2 and boardParameters[8]==sign2:
            gameOver+=1
        elif boardParameters[4]==sign2 and boardParameters[6]==sign2:
            gameOver+=1
    if(gameOver==1):
        print("Player 2 Wins")
    return gameOver

    


print("Welcome to the Tic-Tac-Toe Game")
print(board())
s1,s2 = assigning_players_characters()

while gameplay1(s1,s2)==0:
    # print(gameOver)
    print(gameplay1(s1,s2))


else:
    print("Game Over")


# if(gameplay1(s1,s2)):
#     print("Player 1 Wins")
# elif(gameplay2(s2)):
#     print("Player 2 Wins")