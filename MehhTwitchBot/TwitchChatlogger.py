import socket  ##for connecting
import logging ##for logging chat to a file
from emoji import demojize ## for removing emoji's from the data.


sock = socket.socket() #Create a socket called sock

## variables needed to connect to twitch
server = 'irc.chat.twitch.tv'
port = 6667
nickname ='mehhsecurity'
token = 'PUTITHERE'
channel = '#mehhsecurity'
## End of variables. 

## Actually connecting to twitch
sock.connect((server, port))
sock.send(f"PASS {token}\n".encode('utf-8'))
sock.send(f"NICK {nickname}\n".encode('utf-8'))
sock.send(f"JOIN {channel}\n".encode('utf-8'))

## getting a response from chat and calling it resp
resp = sock.recv(2048).decode('utf-8')

## Setup logging 
logging.basicConfig(level=logging.DEBUG,
					format='%(asctime)s — %(message)s',
                    datefmt='%Y-%m-%d_%H:%M:%S',
                    handlers=[logging.FileHandler('chat.log', encoding='utf-8')])



## Look for messages and log them. If you get the a message that starts with 'PING' reply 'PONG'
while True:
		resp = sock.recv(2048).decode('utf-8')

		if resp.startswith('PING'):
				sock.send('PONG\n'.encode('utf-8'))

		elif len(resp) > 0:
			logging.info(demojize(resp))



