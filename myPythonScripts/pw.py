#! python3
# pw.py  An insecure password locker program
#
##########################################################
import sys,pyperclip

PASSWORDS ={'email':'password@email',
            'blog':'password@blog',
            'tango':'password@tango',
            'test':'test@password'
}

if len(sys.argv) < 2:
    print('Usage: py pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] 

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
    