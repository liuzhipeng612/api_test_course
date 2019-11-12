# 2.请写出if判断语句的格式
"""
答：
    if _____:
        _____

    elif _____:
        _____
    else:
        _____
"""

# 3.求三个整数中的最大值   提示：三个整数使用input提示用户输入
intA = input('输入一个整数A：')
intA = int(intA)
intB = input('输入一个整数B：')
intB = int(intB)
intC = input('输入一个整数C：')
intC = int(intC)

if intA > intB and intA > intC:
    print(intA)
elif intB > intA and intB > intC:
    print(intB)
elif intC > intA and intC > intB:
    print(intC)
else:
    print('输入的整数相等')

# 4.判断是否为闰年
"""
提示：
输入一个有效的年份（如：2019），判断是否为闰年
如果是闰年，则打印“2019年是闰年”；否则打印“2019年不是闰年”
"""

while True:
    years = input('输入一个年份，如2019：')
    years = int(years)
    if years == 0:
        break
    elif years % 4 == 0 and years % 100 != 0:
        print('%d是闰年' % (years,))
    else:
        print('{}不是闰年'.format(years))

# # 5.分别使用for和while打印九九乘法表
# """
# 提示：
# 输出九九乘法表，格式如下：（每项数据之间空一个Tab键，可以使用"\t"）
# """
for multiplicand in range(1, 10):
    expression = ''
    for multiplier in range(1, multiplicand + 1):
        product = multiplicand * multiplier
        expression += '{} * {}={}\t'.format(multiplier, multiplicand, product)
    print(expression)

# 6、你的微信好友当中有 5 个推销的，他们存在一个列表 black_list=['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']
# 当中, 请把这 5 个人从 black_list 当中删除，最后 black_list 为空。

black_list = ['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']
while black_list:  # for为什么不能删除到空呢？列表单个值时却可以删空。
    del black_list[0]
    print(black_list)
# 7.使用if语句完成剪刀石头布游戏
"""
提示：
提示用户输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
电脑随机出拳
比较胜负，显示用户胜、负还是平局
电脑随机出拳
使用随机数，首先需要导入随机数的模块 —— “工具包”
import random
导入模块后，可以直接在 模块名称 后面敲一个"."然后按 Tab键，会提示该模块中包含的所有函数
random.randint(a, b)，返回[a, b]之间的整数，包含a和b
random.randint(1, 10)  # 生成的随机数n: 1 <= n <= 10
random.randint(4, 4)  # 结果永远是 4
random.randint(25, 12)  # 该语句是错误的，下限必须小于上限
"""
import random

while True:
    punch = input("请出拳：")
    punch = int(punch)
    robot = random.randint(1, 3)
    if punch == 0:
        break
    elif (punch < robot and robot - punch == 1) \
            or (punch > robot and robot - punch == -2):
        print("你赢了")
    elif punch == robot:
        print("平局")
    else:
        print("你输了")
# 8.使用循环实现经典冒泡算法
"""
提示：
利用for循环，完成a=[1,7,4,89,34,2]的冒泡排序（小的数字排前面，大的排后面），
不能使用sort、sorted等内置函数或方法
"""
a = [1, 7, 4, 89, 34, 2]
i = 0
while i in range(0, 6):
    if a[i] > a[i + 1]:
        a[i], a[i + 1] = a[i + 1], a[i]
    print(a)
