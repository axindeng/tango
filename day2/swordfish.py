
while True:
    print('who are you?')
    name = input()
    if name != 'Joe':
        print('Wrong Name')
        continue
    print('Hello,Joe.What is your password?(It is a fish)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')