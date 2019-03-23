
import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
#print(mo.group())


numRegex = re.compile(r'''(
    ^\d{1,3}     #1个或者2个数字
    (,\d\d\d)*$  #有或者没有逗号3个数字组合
)''',re.VERBOSE
)
#numRegex = re.compile(r'^\d{1,3}(,\d{3})*$')

nameList = ['42','1,234','6,345,212','22,34,567','2345']

for i in range(len(nameList)):
    mo = numRegex.search(nameList[i])
    if mo == None:
        print(nameList[i] + ' Not match')
    else:
        print(mo.group())


