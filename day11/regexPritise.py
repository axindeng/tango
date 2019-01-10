import re

nameRegex = re.compile(r'''(
(A-Z){1}			#匹配名，首字母必须大写	
(a-zA-Z)*			#匹配名后面部分，必须为字母不能包含其他字符
(\s){1}
(Nakamoto){1}		#匹配姓，必须出现1次
)''',re.VERBOSE
)

nameRegex = re.compile(r'[A-Z][a-z]*\sNakamoto')

nameList = ['Satoshi Nakamoto','Alice Nakamoto','RoboCop Nakamoto','satoshi Nakamoto','Mr. Nakamoto','Nakamoto','Satoshi nakamoto']
#for i in range(len(nameList)):
#    mo = nameRegex.search(nameList[i])
#    if mo == None:
#        print(nameList[i] + 'Not matched.')
#    else:
#        print(mo.group())



jRegex = re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseablls)\.,re.IGNOREACSE')
JList = ['Alice eats apples.','Bob pets cats.','Carol throws baseballs.','Alice throws Apples.','BOB EATS CATS.','RoboCop eats apples.','ALICE THROWS FOOTBALLS.','Carol eats 7 cats.']


for i in range(len(JList)):
    print(JList[i])
    mo = jRegex.search(JList[i])
    if mo == None:
        print(JList[i] + ' Not matched.')
    else:
        print(mo.group())

