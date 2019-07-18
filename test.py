# class MyCalendarThree:
#
#     def __init__(self):
#         self.timeline = collections.OrderedDict()
#
#     def book(self, start: int, end: int) -> int:
#         if start not in self.timeline:
#             self.timeline[start] = 1
#         else:
#             self.timeline[start] += 1
#         if end not in self.timeline:
#             self.timeline[end] = -1
#         else:
#             self.timeline[end] -= 1
#
#         self.timeline = dict(sorted(self.timeline.items(), key = lambda x : x[0]))
#
#         maxBook = 0
#         ongoing = 0
#         for time in self.timeline:
#             ongoing += self.timeline[time]
#             maxBook = max(maxBook, ongoing)
#         return maxBook


# class Solution:
#     def isNStraightHand(self, hand, W):
#         self.hand = hand
#         self.W = W
#         self.hand.sort()
#         # self.b=[]
#         k = len(self.hand) // self.W
#
#         if len(self.hand) % self.W == 0:
#             if self.hand:
#                 self.b = []
#                 self.b.append(min(self.hand))
#                 if (min(self.hand) + 1) in self.hand:
#                     if len(self.b) <= k:
#                         self.b.append(min(self.hand) + 1)
#                 return False
#                 for item in self.b:
#                     self.hand.remove(item)
#                 print(self.hand)
#             return True
#         return False
#
# hand = [1,2,3]
# W=2
# solution = Solution()
# solution.isNStraightHand(hand,W)


# def isNStraightHand(hand, W):
#
#     hand.sort()
#     # self.b=[]
#     k = len(hand) // W
#
#     if len(hand) % W == 0:
#         while hand:
#             b = []
#             b.append(min(hand))
#             while len(b) < k:
#                 if (b[-1] + 1) in hand:
#                     b.append(b[-1] + 1)
#             #return False
#             for item in b:
#                 hand.remove(item)
#             #print(hand)
#         return True
#     return False
#
# hand = [1,2,3,4,5,6,7,8,9]
# W=3
#
# print(isNStraightHand(hand,W))


# class Solution:
#     def findOcurrences(self, text, first, second):
#         self.text = text
#         self.first = first
#         self.second = second
#
#         x = self.text.split()
#         if self.first in x and self.second in x and x.index(second)==x.index(first)+1:
#             return type(x.index(second)+1)
#
# solution = Solution()
# print(solution.findOcurrences("I want to go to American","go","to"))

# class Solution:
#     def countBinarySubstrings(self, s: str) -> int:
#         self.s = s
#         self.counts = 0
#         for i in range(len(self.s)):
#             for j in range(i+1,len(self.s)+1):
#                 if self.s[i:j].count('0')==self.s[i:j].count('1'):
#                     if self.s[i:j].count('0') == 1:
#                         self.counts += 1
#                     elif self.s[i:j].count('0') > 1:
#                         if self.s[self.s.index('0')+1]=='0' and self.s[self.s.index('1')+1]=='1':
#                             self.counts += 1
#         return self.counts


# import numpy as np
#
#
# class Solution:
#     def largestPerimeter(self, A):
#         self.A = A
#         self.max = 0
#         for a in self.A:
#             for b in self.A:
#                 for c in self.A:
#                     if np.sqrt((a+b+c)*(a+b-c)*(a+c-b)*(b+c-a))/4 > self.max:
#                         self.max = np.sqrt((a + b + c) * (a + b - c) * (a + c - b) * (b + c - a)) / 4
#         return self.max
#
# A = [3,5,4]
# solution = Solution()
# print(solution.largestPerimeter(A))


# # 计算1！+2！+3！+ ... +n！
# def mulitply(n):
#     if n == 1:
#         return  1
#     return n*mulitply(n-1)
#
# def result(n):
#     sum = 0
#     for i in range(1,n+1):
#         sum += mulitply(i)
#     return  sum
#
# print(result(10))


# # 给定y和m，计算y年m月有多少天
# def days(y,m):
#     if m in [1,3,5,7,8,10,12]:
#         return 31
#     elif m in [4,6,9,11]:
#         return 30
#     if m == 2:
#         if y % 4 == 0:
#             return 28
#         else:
#             return 29
#
# print(days(2020,2))


# # map函数
# def mul(a):
#     return a*3
#
# def mul2(a,b):
#     return  a*b
#
# list1 = [10,20,30,40,50,60]
# list2 = [6,5,4,3,2,1]
#
# print(list(map(mul,list1)))
# print(list(map(mul2,list1,list2)))
#
# # 匿名函数lambda
# print(list(map(lambda x: 4*x,list1)))
# print(list(map(lambda x,y: x*y,list1,list2)))


# # 水仙花数判定
# def fun(n):
#     a = str(n)
#     b = len(a)
#     sum = 0
#     for i in range(b):
#         sum += int(a[i])**b
#     if sum == n:
#         return True
#     else:
#         return False
#
# print(fun(153))
# print(fun(1634))
#
# def fun2(max):
#     """返回100和max之间的所有水仙花数"""
#     a = []
#     for i in range(100,max+1):
#         if fun(i) == True:
#             a.append(i)
#     return a
#
# print(fun2(2000))


# # 多维数组
# # 初始化多维(10*10)数组
# data = [[0]*10 for j in range(10)]
# print(data)


# 数据可视化

# # 折线图
# import matplotlib.pyplot as plt
#
# input_values = [1,2,3,4,5]
# squares = [1,4,9,16,25]
# plt.plot(input_values,squares,linewidth=5)
#
# # 设置图表标题，并给坐标轴加上标签
# plt.title("Square Numbers",fontsize=24)
# plt.xlabel("Value",fontsize=14)
# plt.ylabel("Square of Value",fontsize=14)
#
# # 设置刻度标记的大小
# plt.tick_params(axis='both',labelsize=14)
#
# plt.show()


# # 散点图
# import matplotlib.pyplot as plt
#
# # x_values = [1,2,3,4,5]
# # y_values = [1,4,9,16,25]
# x_values = list(range(1,1001))
# y_values = [x**2 for x in x_values]
#
# # plt.scatter(x_values,y_values,c=(0,0,0.8),edgecolor='none',s=40)
# plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolor='none',s=40)# 颜色映射（是一系列颜色，从起始颜色渐变到结束颜色）
#
# # 设置图表标题，并给坐标轴加上标签
# plt.title("Square Numbers",fontsize=24)
# plt.xlabel("Value",fontsize=14)
# plt.ylabel("Square of Value",fontsize=14)
#
# # 设置刻度标记的大小
# # plt.tick_params(axis='both',which='major',labelsize=14)
# plt.axis([0,1100,0,1100000])
#
# plt.show()
# # 自动保存图表
# plt.savefig('squares_plot.png',bbox_inches='tight')

# # 15.1
# import  matplotlib.pyplot as plt
#
# x = list(range(1,5000))
# y = [x**3 for x in range(1,5000)]
#
# plt.plot(x,y,linewidth=5)
#
# plt.title("x * x * x",fontsize=24)
# plt.xlabel("Value",fontsize=14)
# plt.ylabel("Value**3",fontsize=14)
#
# plt.show()


# 创建RandomWalk()类
# from random import choice
# import matplotlib.pyplot as plt
#
# class RandomWalk():
#     """一个生成随机漫步数据的类"""
#     def __init__(self,num_points=5000):
#         self.num_points = num_points
#
#         # 所有随机漫步都始于（0,0）
#         self.x_values = [0]
#         self.y_values = [0]
#
#     def fill_walk(self):
#         """计算随机漫步包含的所有点"""
#         # 不断漫步直到列表达到指定的长度
#         while len(self.x_values) < self.num_points:
#
#             # 决定前进方向以及沿这个方向前进的距离
#             x_direction = choice([1,-1])
#             x_distance = choice([0,1,2,3,4])
#             x_step = x_direction * x_distance
#
#             y_direction = choice([1, -1])
#             y_distance = choice([0, 1, 2, 3, 4])
#             y_step = y_direction * y_distance
#
#             # 拒绝原地踏步
#             if x_step == 0 and y_step == 0:
#                 continue
#
#             # 计算下一个点的x值和y值
#             next_x = self.x_values[-1] + x_step
#             next_y = self.y_values[-1] + y_step
#
#             self.x_values.append(next_x)
#             self.y_values.append(next_y)
#
# while True:
#
#     rw = RandomWalk(50000)
#     rw.fill_walk()
#
#     # 设置绘图窗口的尺寸
#     plt.figure(dpi=128,figsize=(10,6))
#
#     point_numbers = list(range(rw.num_points))
#     plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolor='none',s=1)
#
#     # 突出起点和终点
#     plt.scatter(0,0,c='green',edgecolor='none',s=50)
#     plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolor='none',s=50)
#
#     # 隐藏坐标轴
#     plt.axes().get_xaxis().set_visible(False)
#     plt.axes().get_yaxis().set_visible(False)
#
#     plt.show()
#
#     keep_running = input("Make another walk?(y/n): ")
#     if keep_running == 'n':
#         break


# # 15.3
# from random import choice
# import matplotlib.pyplot as plt
#
# class RandomWalk():
#     """一个生成随机漫步数据的类"""
#     def __init__(self,num_points=5000):
#         self.num_points = num_points
#
#         # 所有随机漫步都始于（0,0）
#         self.x_values = [0]
#         self.y_values = [0]
#
#     def fill_walk(self):
#         """计算随机漫步包含的所有点"""
#         # 不断漫步直到列表达到指定的长度
#         while len(self.x_values) < self.num_points:
#
#             # 决定前进方向以及沿这个方向前进的距离
#             x_direction = choice([1,-1])
#             x_distance = choice([0,1,2,3,4])
#             x_step = x_direction * x_distance
#
#             y_direction = choice([1, -1])
#             y_distance = choice([0, 1, 2, 3, 4])
#             y_step = y_direction * y_distance
#
#             # 拒绝原地踏步
#             if x_step == 0 and y_step == 0:
#                 continue
#
#             # 计算下一个点的x值和y值
#             next_x = self.x_values[-1] + x_step
#             next_y = self.y_values[-1] + y_step
#
#             self.x_values.append(next_x)
#             self.y_values.append(next_y)
#
# while True:
#
#     rw = RandomWalk()
#     rw.fill_walk()
#
#     # 设置绘图窗口的尺寸
#     plt.figure(dpi=128,figsize=(10,6))
#
#     point_numbers = list(range(rw.num_points))
#     plt.plot(rw.x_values,rw.y_values,linewidth=10)
#
#     # 突出起点和终点
#     plt.scatter(0,0,c='green',edgecolor='none',s=50)
#     plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolor='none',s=50)
#
#     # 隐藏坐标轴
#     plt.axes().get_xaxis().set_visible(False)
#     plt.axes().get_yaxis().set_visible(False)
#
#     plt.show()
#
#     keep_running = input("Make another walk?(y/n): ")
#     if keep_running == 'n':
#         break


# # 创建Die类，模拟一个骰子
# from random import randint
# import pygal
#
# class Die():
#
#     def __init__(self,num_sizes=6):
#         self.num_sizes = num_sizes
#
#     def roll(self):
#         """返回一个位于1和骰子面数之间的随机数"""
#         return randint(1,self.num_sizes)
#
#
# die = Die()
#
# # 掷几次骰子，把结果保存在列表中
# results = []
# for roll_num in range(1000):
#     results.append(die.roll())
#
# # 分析结果
# frequencies = []
# for value in range(1,die.num_sizes+1):
#     frequencies.append(results.count(value))
#
# # 对结果进行可视化
# hist = pygal.Bar()
#
# hist.title = "Results of rolling one D6 1000 times."
# hist.x_labels = [1,2,3,4,5,6]
# hist.x_title = "Result"
# hist.y_title = "Frequency of Result"
#
# hist.add('D6',frequencies)
# #hist.render_to_file('die_visual.svg')

# list1 = list(range(1,11))
# list1.appendleft(0)
# print(list1[0])


# import numpy as np
# # list1 = [1,2,3,4,5]
# # list1 = np.array(list1)
# # list2 = np.array([2,3,4,5,6])
# # print(list1*list2)
# list_1 = np.ones(4)
# print(list_1)


# print(round(0.1+0.2,1) == 0.3)
# print(float(0.1))
# print(pow(3,pow(3,99),10000) == (9**99)%10000)
# # print((3**(3**99))%10000)
# print(round(3.567,2))


# # daydayupQ3
# dayup = 1.0
# dayfactor = 0.01
# for i in range(365):
#     if i % 7 in [0,6]:
#         dayup *= (1-dayfactor)
#     else:
#         dayup *= (1+dayfactor)
# print("The dayfactor is : {:2f}".format(dayup))

# # daydayupQ4
# dayup = 1.0
# for dayfactor in range(1000):
#     dayfactor /= 1000
#     for i in range(365):
#         if i % 7 in [0,6]:
#             dayup *= (1-0.01 )
#         else:
#             dayup *= (1+dayfactor)
#     if dayup > 37.78:
#         print("The dayfactor is : {:2f}".format(dayfactor))
#         break
# print("The dayup is : {:2f}".format(dayup))


# # unicode编码
# for i in range(12):
#     print(chr(9800+i),end='')


# # time库的使用
# import time
#
# # 获取时间
# print(time.time())
# print(time.ctime())
# t = time.gmtime()
# print(t)
# print(time.strftime("%Y-%m-%d %H:%M:%S",t))
#
# # 程序计时
# start = time.perf_counter()
# end = time.perf_counter()
# print(end-start)


# # 文本进度条
# # TextProBarV1.py
# import time
#
# scale = 10
# print("-----执行开始-----")
# for i in range(scale+1):
#     a = '*' * i
#     b = '.' * (scale - i)
#     c = (i/scale) * 100
#     print("\r{:^3.0f}%[{}->{}]".format(c,a,b),end='')
#     time.sleep(0.5)
# print("\n-----执行结束-----")

# k = 10000
# i = 0
# while k > 1:
#     print(k)
#     k = k/2
#     i += 1
# print(i)

# import random
#
# print(random.random())
# print(random.randint(0,2))
# print(random.getrandbits(1))
# print(random.randrange(1))

# i = 10431
# sum = 0
# for j in str(i):
#     sum += int(j)
# print(sum)


# random库的使用
import random

# # 基本随机数函数
# random.seed(10) #设置随机数的种子
# random.random() #产生0,1之间的随机数
#
# # 扩展随机数函数
# random.randint(10,100) # 产生10,100之间的随机整数
# random.randrange(10,100,10) # 产生10,100之间以10为步长的整数
# random.getrandbits(16) # 生成一个16比特长的随机整数
# random.uniform(10,100) # 生成10,100之间的随机小数
# # 从序列seq中随机选择一个元素
# seq = list(range(1,10))
# random.choice(seq)
# # 将序列seq中元素随机排列，返回打乱后的序列
# s = random.shuffle(seq)
# print(s)

# # 蒙特卡洛方法求圆周率
# from random import random
# from time import perf_counter
#
# num = 1000*1000
# count = 0
# start = perf_counter()
# for time in range(num):
#     x,y = random(),random()
#     if pow(x**2 + y**2,0.5) < 1:
#         count += 1
# pi = 4 * count / num
# print(pi)
# print(perf_counter()-start)


# arr = [3,5,2,8,6]
# arr.sort()
# print(arr)


# 数组排序
# class Solution:
#     def relativeSortArray(self, arr1, arr2):
#         self.arr1 = arr1
#         self.arr2 = arr2
#         self.arr3 = []
#         for i in self.arr1:
#             if i in self.arr2:
#                 pass
#             else:
#                 self.arr3.append(i)
#                 self.arr1.remove(i)
#         self.arr3.sort()
#         self.arr1 += self.arr3
#         print(self.arr1)
# a = [2,3,1,3,2,4,6,7,9,2,19]
# b = [2,1,4,3,9,6]
# solution = Solution()
# solution.relativeSortArray(a,b)


# class Solution:
#     def defangIPaddr(self,address):
#         self.address = address
#         for c in self.address:
#             if c == '.':
#                 c = '[.]'
#         print(self.address)
#
# solution = Solution()
# solution.defangIPaddr('1.1.1.1.1')

# address = '1.1.1.1'
# print(address.replace('.','[.]'))
# # a = []
# # for c in address:
# #     a.append(c)
# #     # if c == '.':
# #     #     c = '[.]'
# print(address)


# class Solution:
#     def backspaceCompare(self, S: str, T: str) -> bool:
#         a = [];b = []
#         for i in S:
#             a.append(i)
#         for j in T:
#             b.append(j)
#
#         while '#' in a:
#             n = a.index('#')
#             if n == 0:
#                 del a[n]
#             del a[n],a[n-1]
#         while '#' in b:
#             n = b.index('#')
#             if n == 0:
#                 del b[n]
#             del b[n],b[n - 1]
#
#         if a == b:
#             return True
#         return False
#
# sol = Solution()
# print(sol.backspaceCompare("a##c","#a#c"))


# n = '00000000000000000000000000001011'
# n = str(n)
# count = 0
# for i in n:
#     if i == '1':
#         count += 1
# print(count)

# a = 'hello'
# b = [];c = [];d = []
# for i in a:
#     b.append(i)
# for i in range(len(b)):
#     if b[i] in 'aeiou':
#         c.append(i)
#         d.append(b[i])
# d.reverse()
# for i in range(len(c)):
#     b[c[i]] = d[i]
# print(''.join(b))


# class Solution(object):
#     def countSegments(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         if s == '':
#             return 0
#         a = s.split(' ')
#         while '' in a:
#             a.remove('')
#         return len(a)
#
# sol = Solution()
# print(sol.countSegments('          '))


# class Solution(object):
#     def findOcurrences(self, text, first, second):
#         """
#         :type text: str
#         :type first: str
#         :type second: str
#         :rtype: List[str]
#         """
#         a = text.split(' ')
#         b = []
#         while first in a and a[a.index(first)+1] == second:
#             b.append(a[a.index(first)+2])
#             del a[a.index(first)+1]
#             a.remove(first)
#         return b
#
# sol = Solution()
# print(sol.findOcurrences("jkypmsxd jkypmsxd kcyxdfnoa jkypmsxd kcyxdfnoa jkypmsxd kcyxdfnoa kcyxdfnoa jkypmsxd kcyxdfnoa","kcyxdfnoa","jkypmsxd"))


# counter = 1
# def doLotsOfStuff():
#     global counter
#     for i in (1, 2, 3):
#         counter += 1
# doLotsOfStuff()
# print(counter)

# import copy
#
# a = [1, 2, 3, 4, ['a', 'b']]
# b = a
# c = copy.copy(a)
# d = copy.deepcopy(a)
# a.append(5)
# a[4].append('c')
# print(a)
# print(b)
# print(c)
# print(d)

# foo = [1,2]
# foo1 = foo
# foo.append(3)
# print(foo,foo1)

# print(r"\nwoow")
# for i in range(6):
#     print(i,end=' ')
# print('\n',len('asfdgh'))

# # 字符串索引
# a = '13.18f'
# print(a[1])

# #TempConvert.py
# TempStr = input("请输入带有符号的温度值: ")
# if TempStr[-1] in ['F', 'f']:
#     C = (TempStr[0:-1] - 32)/1.8
#     print("转换后的温度是{:.2f}C".format(C))
# elif TempStr[-1] in ['C', 'c']:
#     F = 1.8*eval(TempStr[0:-1]) + 32
#     print("转换后的温度是{:.2f}F".format(F))
# else:
#     print("输入格式错误")

# print(ord('A'))

# # 把列表当作队列使用
# from collections import deque
#
# queue = deque(['fafg','yrhc','uixdjg'])
# queue.append('bchr')
# queue.popleft()
# print(queue)

# print([['']*3 for j in range(4)])
# print([['']*3]*4)

# # 转置矩阵
# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# matrix_zhuanzhi = [[row[i] for row in matrix] for i in range(4)]
# matrix_zhuanzhi2 = []
# for i in range(4):
#     matrix_zhuanzhi2.append([row[i] for row in matrix])
# # for i in range(4):# 有问题
# #     for row in matrix:
# #         matrix_zhuanzhi2.append(row[i])
# print(matrix_zhuanzhi)
# print(matrix_zhuanzhi2)

# a = dict(sape=4139, guido=4127, jack=4098)
# print(a)
# for i in a.keys():
#     print(type(i))

# basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# for i,v in enumerate(basket):
#     print(i,v)
# print(sorted(basket))
# print(basket)
# basket.sort()
# print(basket)
#
# import sys
#
# print('命令行参数如下:')
# for i in sys.argv:
#     print(i)
# print('\n\nPython 路径为：', sys.path, '\n')


# a = []
# def list_append():
#     for i in range(10):
#         a.append(i)
#     return a
#
# print(list_append())

# f = lambda x,y:x+y
# print(f(3,8))

# # 绘制七段数码管
# #SevenDigitsDrawV1.py
# import turtle
#
# def drawLine(draw):   #绘制单段数码管
#     turtle.pendown() if draw else turtle.penup()
#     turtle.fd(40)
#     turtle.right(90)
#
# def drawDigit(digit): #根据数字绘制七段数码管
#     drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
#     drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
#     drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
#     drawLine(True) if digit in [0,2,6,8] else drawLine(False)
#     turtle.left(90)
#     drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
#     drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
#     drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
#     turtle.left(180)
#     turtle.penup()
#     turtle.fd(20)
#
# def drawDate(date):  #获得要输出的数字
#     for i in date:
#         drawDigit(eval(i))  #通过eval()函数将数字变为整数
#
# def main():
#     turtle.setup(800, 350, 200, 200)
#     turtle.penup()
#     turtle.fd(-300)
#     turtle.pensize(5)
#     drawDate('20190718')
#     turtle.hideturtle()
#     turtle.done()
#
# main()


# 绘制漂亮的七段数码管
#SevenDigitsDrawV2.py
import turtle,time

def drawGap(): #绘制数码管间隔
    turtle.penup()
    turtle.fd(5)

def drawLine(draw):   #绘制单段数码管
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)

def drawDigit(d): #根据数字绘制七段数码管
    drawLine(True) if d in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if d in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)

def drawDate(date):
    turtle.pencolor("red")
    for i in date:
        if i == '-':
            turtle.write('年',font=("Arial", 18, "normal"))
            turtle.pencolor("green")
            turtle.fd(40)
        elif i == '=':
            turtle.write('月',font=("Arial", 18, "normal"))
            turtle.pencolor("blue")
            turtle.fd(40)
        elif i == '+':
            turtle.write('日',font=("Arial", 18, "normal"))
        else:
            drawDigit(eval(i))

def main():
    turtle.setup(800, 350, 200, 200)
    turtle.penup()
    turtle.fd(-350)
    turtle.pensize(5)
#    drawDate('2018-10=10+')
    drawDate(time.strftime('%Y-%m=%d+',time.gmtime()))
    turtle.hideturtle()
    turtle.done()

main()


# # 递归
# def fact(n):
#     if n == 0:
#         return 1
#     return n*fact(n-1)
#
# print(fact(5))

# 字符串反转
# s = 'abcdefghijk'
# print(s[::-1])
def rvs(s):
    if s == '':
        return s
    else:
        return rvs(s[1:]) + s[0]

# 斐波那契数列
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# 汉诺塔问题
count = 0

def hanoi(n,src,dst,mid):
    global count
    if n == 1:
        print("{}:{}->{}".format(1,src,dst))
        count += 1
    else:
        hanoi(n-1,src,mid,dst)
        print("{}:{}->{}".format(n,src, dst))
        count += 1
        hanoi(n-1,mid,dst,src)

hanoi(10,"A","C","B")
print(count)