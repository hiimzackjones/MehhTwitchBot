import socket, string
import logging ##for logging chat to a file
#from emoji import demojize ## for removing emoji's from the data.

# All the stuff needed for connect
HOST = "irc.twitch.tv"
NICK = "mehhsecurity"
PORT = 6667
PASS = 'oauth:PUTITHERE'
readbuffer = ""
MODT = False

# This is how you connect to IRC
s = socket.socket()
s.connect((HOST, PORT))
s.send("PASS " + PASS + "\r\n")
s.send("NICK " + NICK + "\r\n")
s.send("JOIN #mehhsecurity \r\n")

# Define sending a message
def Send_message(message):
    s.send("PRIVMSG #mehhsecurity :" + message + "\r\n")

#a while true means run forever. 
while True:

    #ADD FULL OUTPUT LOGGING HERE
    #
    # logging may actually go below. 
    #
    #WE NEED LOGGING!!!!


    readbuffer = readbuffer + s.recv(1024)
    temp = string.split(readbuffer, "\n")
    readbuffer = temp.pop()

    for line in temp:
        # afk checking
        if (line[0] == "PING"):
            s.send("PONG %s\r\n" % line[1])
        # regular chat stuff starts here.     
        else:
            # Splits the given string so we can work with it better
            parts = string.split(line, ":")

            if "QUIT" not in parts[1] and "JOIN" not in parts[1] and "PART" not in parts[1]:
                try:
                    # Sets the message variable to the actual message sent
                    message = parts[2][:len(parts[2]) - 1]
                except:
                    message = ""
                # Sets the username variable to the actual username
                usernamesplit = string.split(parts[1], "!")
                username = usernamesplit[0]
                
                # Only works after twitch is done announcing stuff (MODT = Message of the day)
                if MODT:
                    print username + ": " + message
                    
                    # You can add all your plain commands here
                    if message == "BENAS":
                        Send_message("YOU FOUND ME. I AM A ROBOT THAT RESPONSE TO THE KEYWORD, THIS MESSAGE WAS SENT BY THE BOT HEHEHEHEHE @" + username)

                for l in parts:
                    if "End of /NAMES list" in l:
                        MODT = True