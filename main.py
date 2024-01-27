import os
import sys
from argparse import ArgumentParser
from send import script_to_list, send_script
from time import sleep
from typing import List

parser = ArgumentParser(
	prog='Discord Send Script',
	description='Code to send entire scripts to Discord text channels.',
	# epilog=''
)

parser.add_argument(
	'filename', type=str,
	help="the filename of the script inside the 'scripts' directory"
)
parser.add_argument(
	'channel_id', type=int,
	help='ID of the text channel where the script will be sent'
)
parser.add_argument(
	'token', type=str,
	help='token of the user'
)
parser.add_argument(
	'-d', '--delay', metavar='TIME', type=float, default=1.0,
	help='delay before sending another message (in seconds)'
)
parser.add_argument(
	'-v', '--verbose', action='store_true',
	help='prints in the terminal the lines sent, the ID of all messages sent and its content'
)

args = parser.parse_args()


def main():
	file_path: str = os.path.abspath(__file__)
	dir_path: str = os.path.dirname(file_path)
	path: str = f'{dir_path}/scripts/{args.filename}'
	
	if not os.path.exists(path):
		raise FileNotFoundError('The file does not exist')
	
	if not os.path.isfile(path):
		raise IsADirectoryError('The specified path is a directory, not a file')
	
	with open(path, 'r') as file:
		raw_script: str = file.read()
		script: List[str] = script_to_list(raw_script)
		lines_sent: int = 0
	
	print(f'Sending {len(script)} lines...')
	
	try:
		for response in send_script(args.token, args.channel_id, script):
			response.raise_for_status()
			lines_sent += 1
			
			if args.verbose:
				message: dict = response.json()
				print(f"Line: {lines_sent} | ID: {message['id']}\n{message['content']}", end='\n\n')
			
			sleep(args.delay)
	except KeyboardInterrupt:
		print('Interrupted.')
	
	print(f'Done sending script! ({lines_sent} lines)')
	
	sys.exit(0)

if __name__ == '__main__':
	main()
