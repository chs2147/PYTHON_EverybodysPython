#! python3
# password_locker.py - An insecure password locker program

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

import sys
import pyperclip


if len(sys.argv) < 2:
    print("Usage: python password_locker.py [account] - copy account password")
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS.keys():
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' coped to clipboard.')
else:
    print("There is no account named: " + account)

