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

# 从文本中查找所有的电话号码，把结果存放在一个列表里面
phoneNumMatches = phoneNumRegex.findall(text)
if  len(phoneNumMatches) <= 0:
    print('phoneNumber match nothing.')
else:
    for i in range(len(phoneNumMatches)):
        print(phoneNumMatches[i])
   
# 从文本中查找所有的email地址，把结果放在一个列表里面
emailMatches = emailRegex.findall(text)
if  len(emailMatches) <= 0:
    print('email match nothing.')
else:
    for i in range(len(emailMatches)):
        print(emailMatches[i])   

# 把列表合并，并转化为字符串，然后拷贝到粘贴板
matchesList = phoneNumMatches + emailMatches

if len(matchesList) > 0:
    matches = '\n'.join(matchesList)
    pyperclip.copy(matches)
else:
    print('Not copy yet.')