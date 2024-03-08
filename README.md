# CSCE4653-HW3
!READ THE NOTE AT THE BOTTOM!

Programming project utilizing a python3 client/server model to manage 
a two-sided interaction. Working with 'sys' and 'socket' modules.

The client-side python file uses a TCP protocol and can only be ran after the server with the corresponding port
is already on. The client will uses the command line to 'guess' certain characters, and based on the input, the server
will respond with an updated line for the client. The client has a set amount of guesses and has a win or lose condition.

The serve-side python file uses TCP protocol as well and can be ran before the client. This server will send socket encodings
over to the client who will then receive them (.recv) and will have to decode the messages. Theses socket encodings are sent
back and forth between server and client during the course of the game. The game intelligence lies within the server and gives
the game rules, title, and current status to the client as they input characters.

NOTE: This server/client sometimes ends up with the client indefinitely stalling. To remedy this, kill only the terminal with the
clientPOLK.py file running, and restart. The server program will end and will need to be started again, but you can keep that terminal
open. This should fix the issue and allow the game to run correctly. If it does not fix it, try it again please, because it will work eventually.
