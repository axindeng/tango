#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: axindeng@qq.com

'''
编写一个名为collatz()的函数，它有一个名为number的参数。如果参数是偶数，那么collatz()就打印出number // 2，并返回该值。如果number是奇数，collatz()就打
印并返回3 * number + 1。 然后编写一个程序，让用户输入一个整数，并不断对这个数调用collatz()，直到函数返回值１（令人惊奇的是，这个序列对于任何整数都有效，利用这个序列，
你迟早会得到1！既使数学家也不能确定为什么。你的程序在研究所谓的“Collatz序列”，它有时候被称为“最简单的、不可能的数学问题”）。
'''

def collatz(number):
    if number % 2 == 0:
        result = number // 2
        print( result )
        return result
    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result
    else:
        return None

'''
在前面的项目中添加try 和except语句，检测用户是否输入了一个非整数的字符串。正常情况下，int()函数在传入一个非整数字符串时，会产生ValueError错误，
比如int('puppy')。在except子句中，向用户输出一条信息，告诉他们必须输入一个整数。
'''


try:
    getNumber = int(input('Enter number:'))
    while True:
        getNumber = collatz(getNumber)
        if getNumber == 1:
            break
except ValueError:
    print('Value Type Error,Try int type.')



