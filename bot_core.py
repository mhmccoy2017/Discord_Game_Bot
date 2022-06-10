import sys
import bot_command_logic as core
from time import sleep



if __name__ == '__main__':
	try:
		core.run_bot()
	except KeyboardInterrupt:
		sys.exit(0)

