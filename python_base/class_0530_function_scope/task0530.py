# 1.函数有哪几种参数类型，分别有什么特点和作用？
"""
答：
    参数类型：形参、实参、位置函数、关键字函数、默认函数、不定长参数（*args、**kwargs）
    特点：
        形参：占坑，函数内参数
        实参：函数调用的具体值
        位置：实参和形参排序一一对应，不能多不能少
        关键字：给参数赋值，方便调用，不用考虑位置关系
        默认函数：给形参赋值，如果实参有值，采用实参值，如果没有，采用形参值，减少实参的调用。
        不定长：可以使用不限实参个数，*args脱衣为元组，**kwargs脱衣为字典
"""

# 2.函数的可变参数是什么？有哪几种？为什么要使用可变参数？
"""
答：
    可变参数：调用函数可以使用不定个数的实参
    种类：*args和**kwargs
    为什么使用：可以使用不限实参个数，*args脱衣为元组，**kwargs脱衣为字典
"""

# 3.将两个变量的值进行交换（a = 100, b = 200）交换之后，a = 200， b = 100

# 2在函数内对全局变量重新赋值
a = 100
b = 200


def exchange():
    global a
    a = 200
    global b
    b = 100


exchange()
print(a, b)

# 3全局变量传入函数变为局部变量并重新赋值，然后返回局部变量的值给函数
a = 100
print(id(a))
b = 200
print(id(b))


def exchange(a, b):
    a = 200
    b = 100
    print(id(a))
    print(id(b))
    return a, b


a, b = exchange(a, b)
print(a, b)
print(id(a))
print(id(b))
print(exchange(a, b))


# 4. 将用户输入的所有数字相乘之后对20取余数,用户输入的数字个数不确定

def remainder(*args):
    d_args = 1
    for i in args:
        d_args = d_args * i
    d_remainders = d_args % 20
    print(d_remainders)


remainder(12, 21, 32)


# 5、编写函数，检查传入列表的长度，如果大于2，那么仅仅保留前两个长度的内容，并将新内容返回
def len_content(*args):
    if len(args) > 2:
        return args[0], args[1]
    else:
        return args


listA = [1, 2, 3]
print(len_content(*listA))


# 6、定义一个函数，传入一个字典和字符串，判断字符串是否为字典中的值，如果字符串不在字典中，则添加到字典中，并返回新的字典
def in_content(str, dict):
    if not str in dict.values():
        dict[len(dict) + 1] = str
        return dict
    else:
        return '字符串在字典值里面'


string = 'c'
dictionary = {1: 'a', 2: 'b'}
print(in_content(string, dictionary))


# 7、通过定义一个计算器函数，调用函数传递两个参数，然后提示选择【1】加 【2】减【3】乘 【4】除 操作，选择之后返回对应操作的值。
def num(nums):
    """判断输入文本是否整数或浮点数，直到输入正确并返回浮点数"""
    while not (nums.isdigit() or nums.replace(".", "").isdigit()):
        print("输入有误，请重新输入！")
        nums = input("请重新输入：")
    return float(nums)


def add_calculator(number1, number2):
    """加法函数"""
    return number1 + number2


def reduce_calculator(number1, number2):
    """减法函数"""
    return number1 - number2


def multiply_calculator(number1, number2):
    """乘法函数"""
    return number1 * number2


def except_calculator(number1, number2):
    """除法函数"""
    if number1 == 0 or number2 == 0:
        return '0不能作为除数和被除数，请重新输入'
    return number1 / number2


def op_calculator(number1, number2):
    print('选择【1】加;【2】减;【3】乘 ;【4】除,输入"q"退出程序')
    option = input('请选择：')
    option = num(option)
    if option == 1:
        return add_calculator(number1, number2)
    elif option == 2:
        return reduce_calculator(number1, number2)
    elif option == 3:
        return multiply_calculator(number1, number2)
    elif option == 4:
        return except_calculator(number1, number2)
    else:
        return '请选择：'


while True:
    """循环输入"""
    number1 = input("请输入一个数字：")
    if number1 == 'q':
        break
    number1 = num(number1)
    number2 = input("请再次输入一个数字：")
    if number2 == 'q':
        break
    number2 = num(number2)
    input_number = op_calculator(number1, number2)
    print(input_number)
    continue


# 8、一个足球队在寻找年龄在15岁到22岁的女孩做拉拉队员（包括15岁和22岁）加入。编写一个程序，询问用户的性别和年龄，
# 然后显示一条消息指出这个人是否可以加入球队，询问10次后，输出满足条件的总人数。


def player():
    meet = []
    for j in range(1, 11):
        gender = input('请输入性别：')
        age = input('请输入年龄：')
        age = int(age)
        if gender == 'girl' and (15 <= age <= 22):
            meet.append('True')
        print('第{}次筛选\n'.format(j))
    return meet.count('True')


print(player())
