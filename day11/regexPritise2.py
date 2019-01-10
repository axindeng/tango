import re

passwd = input('Please input your password. ')

def checkpwd(passwd):
    if len(passwd) < 8:
        print('不满足8个以上字符的要求:')
    check1 = re.compile('.*[a-z]+.*')
    check2 = re.compile('.*[A-Z]+.*')
    check3 = re.compile('.*(\d){1,}.*')
    check1Result = check1.search(passwd)
    check2Result = check2.search(passwd)
    check3Result = check3.search(passwd)
    if check1Result == None:
        print('不满足小写字母要求')
    if check2Result == None:
        print('不满足大写字母要求')
    if check3Result == None:
        print('不满足1个数字的要求')
    if (check1Result == None) or (check2Result == None) or (check3Result == None):
        print('你输入的密码不符合要求')
    else:
        print('你输入的密码符合要求！')

checkpwd(passwd)
