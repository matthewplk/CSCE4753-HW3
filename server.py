'''This Server shall hold all of the game intelligence, while the player "aka" client should do
the work of sending in characters in this game to guess ARKANSAS. Below is Hangman logic;


 |----|     <-- 1.
 |    0     <-- 2.
 |   -|-    <-- 6, 3, 7.
 |    ^   <-- 4, 5. (/ -> ^)
_|____

'''

import sys
from socket import *

goal = 'ARKANSAS' #8 letters, 3 A's, 2 S's.
startWord = '--------'
currList = list(startWord)
answerList =list(goal)
currWord = ''


guess = 8
wrongs = 0
wrongList = []

if sys.argv.__len__() != 2:
    gamePort = 25730 #5555
else:
    gamePort = int(sys.argv[1])

gameSocket = socket(AF_INET, SOCK_STREAM)

gameSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

gameSocket.bind(('', gamePort))

gameSocket.listen(1) # 1 player allowed.

print("Waiting for players...")
connectionSocket, addr = gameSocket.accept() # Pick up Player 1

PropInfo = "HANGMAN: Guess the 8-Letter Word!"
Title = PropInfo.encode('utf-8')
connectionSocket.send(Title)

try:
    # Forever, read in sentence, convert to uppercase, and send
    while guess >= 0 and wrongs <= 7: #might need and.
        # This keeps track of the list so far.
        print(currList)
        clientString = ''.join(map(str,currList))
        ToClient = clientString.encode('utf-8')
        connectionSocket.send(ToClient)

        if currList == answerList:
            print("You win!!")
            print("CLOSING CLIENT CONNECTION.")
            # Close connection to client but do not close welcome socket
            connectionSocket.close()
            break

        elif guess == 0:
            print("You ran out of guesses!")
            print("CLOSING CLIENT CONNECTION.")
            # Close connection to client but do not close welcome socket
            connectionSocket.close()
            break

        elif wrongs == 7:
            print("HANGMAN! You got too many wrong!")
            print("CLOSING CLIENT CONNECTION.")
            # Close connection to client but do not close welcome socket
            connectionSocket.close()
            break

        match wrongs:
            case 0:
                print("\nIncorrect Guesses Made: %2d" % (wrongs))
                print("\n        ")
                print("\n |      ")
                print("\n |      ")
                print("\n |      ")
                print("\n |      ")
                print("\n_|_____ ")
            case 1:
                print("\nIncorrect Guesses Made: %2d" % (wrongs))
                print("\n        ")
                print("\n |---|  ")
                print("\n |      ")
                print("\n |      ")
                print("\n |      ")
                print("\n_|_____ ")
            case 2:
                print("\nIncorrect Guesses Made: %2d" % (wrongs))
                print("\n        ")
                print("\n |---|  ")
                print("\n |   0  ")
                print("\n |      ")
                print("\n |      ")
                print("\n_|_____ ")
            case 3:
                print("\nIncorrect Guesses Made: %2d" % (wrongs))
                print("\n        ")
                print("\n |---|  ")
                print("\n |   0  ")
                print("\n |   |  ")
                print("\n |      ")
                print("\n_|_____ ")
            case 4:
                print("\nIncorrect Guesses Made: %2d" % (wrongs))
                print("\n        ")
                print("\n |---|  ")
                print("\n |   0  ")
                print("\n |   |  ")
                print("\n |  /   ")
                print("\n_|_____ ")
            case 5:
                print("\nIncorrect Guesses Made: %2d" % (wrongs))
                print("\n        ")
                print("\n |---|  ")
                print("\n |   0  ")
                print("\n |   |  ")
                print("\n |   ^  ")
                print("\n_|_____ ")
            case 6:
                print("\nIncorrect Guesses Made: %2d" % (wrongs))
                print("\n        ")
                print("\n |---|  ")
                print("\n |   0  ")
                print("\n |  -|  ")
                print("\n |   ^  ")
                print("\n_|_____ ")
            case 7:
                print("\nIncorrect Guesses Made: %2d" % (wrongs))
                print("\n        ")
                print("\n |---|  ")
                print("\n |   0  ")
                print("\n |  -|- ")
                print("\n |   ^  ")
                print("\n_|_____ ")
                

        # Read bytes from socket
        playerChar = connectionSocket.recv(1024) # receive the encoded byte message char from player
        currWordPart = playerChar.decode('utf-8') # decode byte message char from player
        playerWordUP = currWordPart.upper() # convert to uppercase

        guess -= 1 # decrease allowed guess count

        print("Guess Count: %2d" % (guess))

        match playerWordUP:
            case 'A':
                currList[0] = 'A'
                currList[3] = 'A'
                currList[6] = 'A'
                CorrectA = "A was in the word!"
                sendCorrectA = CorrectA.encode('utf-8')
                connectionSocket.send(sendCorrectA)
            case 'R':
                currList[1] = 'R'
                CorrectR = "R was in the word!"
                sendCorrectR = CorrectR.encode('utf-8')
                connectionSocket.send(sendCorrectR)
            case 'K':
                currList[2] = 'K'
                CorrectK = "K was in the word!"
                sendCorrectK = CorrectK.encode('utf-8')
                connectionSocket.send(sendCorrectK)
            case 'N':
                currList[4] = 'N'
                CorrectN = "N was in the word!"
                sendCorrectN = CorrectN.encode('utf-8')
                connectionSocket.send(sendCorrectN)
            case 'S':
                currList[5] = 'S'
                currList[7] = 'S'
                CorrectS= "S was in the word!"
                sendCorrectS = CorrectS.encode('utf-8')
                connectionSocket.send(sendCorrectS)
            case _:
                wrongList.append(playerWordUP)
                wrongs +=1
                WrongsMSG = "Your letter is WRONG."
                WrongMSGsent = WrongsMSG.encode('utf-8')
                connectionSocket.send(WrongMSGsent)


        Tt1 = connectionSocket.recv(1024) 
        t1 = Tt1.decode('utf-8')

  
finally:
    print("CLOSING CLIENT CONNECTION AGAIN.")
    # Close connection to client but do not close welcome socket
    connectionSocket.close()
    gameSocket.close()
    print("CLIENT CONNECTION IS CLOSED AGAIN.")
