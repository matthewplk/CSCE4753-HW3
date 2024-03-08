'''
This is where the player/client will connect and send over to the server a guess of a 'char'.
'''
import sys

# Import socket library
from socket import *

# Set hostname or IP address from command line or default to localhost
# Set port number by converting argument string to integer or use default
# Use defaults
if sys.argv.__len__() != 3:
    serverName = 'localhost'
    serverPort = 25730 #5555
# Get from command line
else:
    serverName = sys.argv[1]
    serverPort = int(sys.argv[2])

# Choose SOCK_STREAM, which is TCP
playerSocket = socket(AF_INET, SOCK_STREAM)

# Connect to server using hostname/IP and port
print("Before the playerSocket connects.")
playerSocket.connect((serverName, serverPort)) # They connect to the server.
print("After the playerSocket connects, before sending receive for gameTitle.")
sentTitle = playerSocket.recv(1024)
gameTitle = sentTitle.decode('utf-8')
print("gameTitle has been recv!")
print(gameTitle)

guessCount = 8
wrongs = 0

try:
    print("Before Client While Loop")
    while wrongs <= 7 and guessCount >= 0: #ADDED THERE IS NO WRONGS UPDATING.

        print("Before currentList is updated.\n")
        sentList = playerSocket.recv(1024) #ADDED
        currentList = sentList.decode('utf-8')
        print(currentList + ", Guesses Left: %2d" % (guessCount))

        if currentList == "ARKANSAS":
            print("You win!!")
            print("CLOSING SERVER CONNECTION.")
            # Close connection to client but do not close welcome socket
            playerSocket.close()
            print("SERVER CONNECTION IS CLOSED.")
            break

        elif guessCount == 0:
            print("You Lose! You ran out of guesses!")
            print("CLOSING SERVER CONNECTION.")
            # Close connection to client but do not close welcome socket
            playerSocket.close()
            print("SERVER CONNECTION IS CLOSED.")
            break

        elif wrongs == 7:
            print("HANGMAN! You lose! You got too many wrong!")
            print("CLOSING SERVER CONNECTION.")
            # Close connection to client but do not close welcome socket
            playerSocket.close()
            print("SERVER CONNECTION IS CLOSED.")
            break

        

        print("Inside the client Loop")
        # Get sentence from user
        letterGuess = input('Guess a letter one at a time in the word: ')

        print("After Input, before encoding.")
        # Send it into socket to server
        guessBytes = letterGuess.encode('utf-8')
        print("After encoding, before sending.")
        playerSocket.send(guessBytes)
        print("After SEND!!!") 

        # Receive response from server via socket
        print("Before recv.")
        sentGameState = playerSocket.recv(1024)
        currGameState = sentGameState.decode('utf-8')
        print(currGameState)
        if currGameState == "Your letter is WRONG.":
                wrongs +=1

        
        print("After recv.")

        test = "t1" #TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
        t1 = test.encode('utf-8')
        playerSocket.send(t1)

        guessCount -= 1


finally:
    print("ENDING SESSION...")
    playerSocket.close()


