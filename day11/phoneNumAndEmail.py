# 导入模块
import pyperclip,re

# 获取粘贴板的文本
text = str(pyperclip.paste())

# 创建电话号码的正则表达式
phoneNumRegex = re.compile(r'''(
    \d{3,}       #区号
    -           #连接字符
    \d{7,}      #电话号码
    -           #连接字符
    \d{1,}      #分机号码
    )
''',re.VERBOSE)


# 创建邮箱的正则表达式
emailRegex  = re.compile(r'''(
    [a-zA-Z0-9]{1,}    # 用户名
    @               # 
    [a-zA-z0-9]{1,}    # 域名
    .               # .
    [a-zA-Z]{2,4}   # 域名后缀
)
''',re.VERBOSE)

phoneNumMatches = phoneNumRegex.findall(text)
if  len(phoneNumMatches) <= 0:
    print('phoneNumber match nothing.')
else:
    for i in range(len(phoneNumMatches)):
        print(phoneNumMatches[i])
   

emailMatches = emailRegex.findall(text)
if  len(emailMatches) <= 0:
    print('email match nothing.')
else:
    for i in range(len(emailMatches)):
        print(emailMatches[i])   


matchesList = phoneNumMatches + emailMatches

if len(matchesList) > 0:
    matches = '\n'.join(matchesList)
    pyperclip.copy(matches)
else:
    print('Not copy yet.')