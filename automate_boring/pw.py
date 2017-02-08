#! python3
# pw.pw - An insecure password program

PASSWORDS = {'email': 'FJfer35mT53OP524afb',
             'blog': '535AF5sfd53596Fba',
             'locker': '51495'
             }

import sys, pyperclip
if len(sys.arg) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]
