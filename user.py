#put your username here
import re
LINES = open("user.txt").readlines()
USER= re.sub(r'\n', '', LINES[0])
REMOTE_PATH =   re.sub(r'\n', '', LINES[1])
