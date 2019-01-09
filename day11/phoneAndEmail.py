#
#
import


# create phoneNumber regex
phoneNumRegex = re.compile(r'''
    \d{3,}          # 区号
     -              # 连接符号
    \d{7,}          # 7位以上的电话号码
     -              # 连接符号
    \d{1,}          # 1位以上的分机号
''',re.VERBOSE)

# create email regex
emailRegex = re.compile(r'''
    \w{1,}          # 用户名，1位以上的英文字母
    @
    \w{1,}          # 域名，1位以上的英文字母
    .
    (com|cn|net|com.cn|org)   # 邮件后缀
''',re.VERBOSE)

# find matches in the clipboard text.



# copy the result to the clipboard

