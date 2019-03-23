import random
import copy
# 需要生成35份试卷
# 每份试卷都随机生成50道选择题，每个选择题有4个答案选项，其中只有1个是正确答案



# The quiz data. Keys are states and values are their capitals.
# 测试的数据表，Keys是州名，Values是州府
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix','Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee','Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City','Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'WestVirginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# TODO0 取得一个随机的州名列表,取得一个随机的州府列表
statesList = list(capitals.keys())
random.shuffle(statesList)
capitalsList = list(capitals.values())

ABCD = ['A','B','C','D']
quizAnswer = []

# TODO1 生成随机的测试卷

# TODO1-1 生成1份随机的测试卷
# 生成试卷头
# 根据随机州名列表，生成试卷题目
# 根据随机州名列表，生成对应1个正确答案选项+3个错误答案选项
# 随机打乱4个答案选项
# 最后将以上内容写入到quiz.txt
quizFile = open('quiz.txt','w')
quizAnswerFile = open('quizAnswerFile.txt','w')
print('Name:')
print('LearnNo.:')
print('\n')
quizFile.write('Name:' + '\n')
quizFile.write('LearnNo.:' + '\n')
quizFile.write('\n')

for i in range(len(statesList)):
    stateName = statesList[i]
    j = i + 1
    print( str(j) + '.What is the capital of ' + stateName + '?')
    quizFile.write(str(j) + '.What is the capital of ' + stateName + '?' + '\n')
    RightAnswer = capitals[stateName]
    wrongAnswerList = copy.copy(capitalsList)       # 拷贝一份所有的答案选项
    wrongAnswerList.remove(RightAnswer)             # 从所有的答案选项中剔除正确的选项，得到错误的选项列表
    wrongAnswerList = random.sample(wrongAnswerList,3) # 从错误选项中随机选取3个选项
    answerList = wrongAnswerList + [RightAnswer]
    random.shuffle(answerList)

    for i in range(len(answerList)):        
        if answerList[i] == RightAnswer:
            print( ABCD[i]+ '. ' + answerList[i] + ' **')
            quizFile.write(ABCD[i]+ '. ' + answerList[i] + ' **' + '\n')
            answer=str(j) + '.' + ABCD[i]
            quizAnswer.append(answer)
        else:
            print( ABCD[i]+ '. ' + answerList[i])
            quizFile.write(ABCD[i]+ '. ' + answerList[i] + '\n')
    quizFile.write('\n')        
    print('\n')


print('Quiz Answer')
for a in quizAnswer:
    quizAnswerFile.write(a + '\n')
    print(a)

quizFile.close()
quizAnswerFile.close()



# TODO1-2 循环生成35份测试卷

# TODO2 根据随机生成的州名列表，生成测试卷对应的答案
# 将内容写入到quizAnswer.txt