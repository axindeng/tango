
import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
#print(mo.group())


numRegex = re.compile(r'''(
    \d{1,3}     #1个或者2个数字
    (\,\d\d\d)*  #有或者没有逗号3个数字组合
)''',re.VERBOSE
)

mo = numRegex.search('42')
print(mo.group())

mo = numRegex.search('1,234')
print(mo.group())


mo = numRegex.search('6,345,321')
print(mo.group())


mo = numRegex.search('22,34,567')
print(mo.group(0))


mo = numRegex.search('2234')
print(mo.group(0))
