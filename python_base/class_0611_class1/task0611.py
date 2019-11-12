#!/usr/bin/env python
# coding=UTF-8
"""
@Author: Cautious Eureka
@Contact: Eureka@Faisen.com
@Project: cautious_eureka
@File: task0611.py
@Time: 2019-06-13 22:43
@Desc: Python full stack automation test engineer(Cautious Eureka)
"""

# 1、实现一个手机类，并实例化你的手机。
"""
共有属性：Color, screen, camera
实例属性：Brand, model, system type
实行行为：Call, text, take pictures
"""


class MobilePhone:
    screen = 'Touch'
    camera = 'Megapixel'

    def __init__(self, brand, color, model='Smartphone', system_type='Android', cellphone_number=''):
        self.brand = brand
        self.color = color
        self.model = model
        self.system_type = system_type
        self.cellphone_number = cellphone_number
        print('品牌：{}，颜色：{}，类型：{}，系统：{}'.format(brand, color, model,
                                               system_type))

    def card(self):
        cellphone_number = self.cellphone_number
        return cellphone_number

    def call(self, caller, answer):
        print('{}使用{}号码打电话给{}'.format(caller, self.card(), answer))

    @staticmethod
    def gap():
        print('\n\\\\', '*' * 69, '\n')


daodao_phone = MobilePhone('Daodao', 'black')
print('类属性1：', MobilePhone.screen)
print('类属性2：', MobilePhone.camera)
friend_phone = MobilePhone('Friend', 'yellow', system_type='IOS', cellphone_number='13888888888')
friend_phone.call('Friend', 'Daodao')
daodao_phone.gap()

# 2、灰色的Tom猫，今年1岁，吃着美味的食物，喝着可口的饮料，非常享受的样子
"""
a.根据以上信息，抽象出一个类
b.定义相关属性，并能在类的外面调用
c.定义相关方法，在方法中打印相应信息
"""


class Cat:
    head = '一个猫头'
    foot = '四只脚'
    tail = '一条尾巴'
    skin = '皮肤多毛'
    print('这是有{},{}，{}，{}的一只猫'.format(head, foot, tail, skin))

    def __init__(self, color, name, age):
        self.color = color
        self.name = name
        self.age = age
        print('{}的{}猫，今年{}岁'.format(color, name, age))

    def eating(self, food):
        self.food = food
        return '{}的{}猫，今年{}岁,吃着美味的{}'.format(self.color, self.name, self.age, food)

    def enjoying(self, enjoy):
        print(self.eating(self.food), '非常享受的样子'.format(enjoy))


daodao_cat = Cat
print('类属性1：', daodao_cat.head)
print('类属性2：', daodao_cat.foot)
print('类属性3：', daodao_cat.tail)
print('类属性4：', daodao_cat.skin)
daodao_phone.gap()
duoduo_cat = Cat('黄色', 'Tom', 2)
print(duoduo_cat.eating('猫粮'))
duoduo_cat.enjoying('享受')
daodao_phone.gap()

# 3.列举3个生活中类和对象的例子，用代码表示。
"""
人类 男人女人
车   公交车 轿车 
树   枫树 杨树
"""


class Mankind:
    hand = '两只手'
    foot = '两只脚'
    print('人类有{}{}'.format(hand, foot))

    def __init__(self, gender, height):
        self.gender = gender
        self.height = height
        print('这个是身高{height}米的{gender}'.format(gender=gender, height=height))

    def work(self, to_work):
        print('这个是身高{1}米的{0}，他正在{2}'.format(self.gender, self.height, to_work))


tom = Mankind('男人', 2)
print(tom.hand)
print(tom.foot)
tom.work('工作')
daodao_phone.gap()


class Car:
    engine = '2.0T'
    wheel = '四个轮子'
    print('车具有一个{}发动机,{}'.format(engine, wheel))

    def __init__(self, brand, color, types):
        self.brand = brand
        self.color = color
        self.types = types
        print('这是一个具有{0}发动机，{1}，品牌是{2}，{3}的{4}'.format(Car.engine, Car.wheel, brand, color, types))

    def drive(self, driver, passenger):
        print('{}开着一个具有{}发动机，{}，品牌是{}，{}的{}载着{}'.format(driver, Car.engine, Car.wheel, self.brand, self.color,
                                                        self.types, passenger))


cnCar = Car
enCar = Car('法拉利', '金色', '跑车')
enCar.drive('刀刀', '树树')
daodao_phone.gap()


class Tree:
    root = '树根'
    leaf = '树叶'
    print('树有{},有{}'.format(root, leaf))

    def __init__(self, types, color, size):
        self.types = types
        self.color = color
        self.size = size
        print('这是有很多{}和{}，{}的一棵{}{}'.format(Tree.root, Tree.leaf, size, color, types))

    def shake(self, wind):
        print('这是有很多{}和{}，{}的一棵{}{}被{}吹的刷刷响'.format(Tree.root, Tree.leaf, self.size, self.color, self.types, wind))


big_tree = Tree
skyscraper = Tree('古榕树', '金黄色', '超大')
skyscraper.shake('大风')
daodao_phone.gap()

# 4.编写如下程序
"""
创建一个名为 Restaurant的类，要求拥有饭店名（restaurant_name） 和美食种类（cooking_type）两个属性。
a.需要创建一个名为 describe_restaurant()的方法（描述饭店名和美食种类相关信息）和一个名为 open_restaurant()的方法（显示饭店正在营业）。
b.根据这个类创建一个名为 restaurant 的实例，分别打印其两个属性，再调用前述两个方法。
"""


class Restaurant:
    def __init__(self, restaurant_name, cooking_type):
        self.restaurant_name = restaurant_name
        self.cooking_type = cooking_type

    def describe_restaurant(self):
        return '这家店的名称是{}，有很多的{}'.format(self.restaurant_name, self.cooking_type)

    def open_restaurant(self, operate):
        return '{}，{}。'.format(self.describe_restaurant(), operate)


restaurant = Restaurant('北京饭店', '中餐')
print(restaurant.describe_restaurant())
print(restaurant.open_restaurant('正在营业'))
daodao_phone.gap()


# 5.编写如下程序
# 编写一个数学计算类，要求初始化方法带参数（传两个数字），能够实现加减乘除运算（方法）。

class Calculate:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def count(self, method):
        """
        选择运算方法执行运算
        :param method: 选择【1】加;【2】减;【3】乘 ;【4】除
        :return: 返回对应的计算结果
        """
        try:
            if method == 1:
                return self.num1 + self.num2
            elif method == 2:
                return self.num1 - self.num2
            elif method == 3:
                return self.num1 * self.num2
            elif method == 4:
                if self.num1 == 0 or self.num2 == 0:
                    return '0不能作为除数或被除数'
                return self.num1 / self.num2
            else:
                return '运算方法有误，请确认选项'
        except TypeError:
            return '输入有误，请输入数字'


daoao_count = Calculate(5, 0)
print(daoao_count.count(2))
daodao_phone.gap()

# 二、选作题
"""
1.编写如下程序
编写一个工具箱类，需要有工具的名称、功能描述、价格，能够添加工具、删除工具、查看工具，并且能获取工具箱中工具的总数。
"""


class Tool:
    def __init__(self, name, function, price):
        self.name = name
        self.function = function
        self.price = price

    def look(self):
        return '这个工具名称:{},功能：{}，价格：{}'.format(self.name, self.function, self.price)

    def __repr__(self):
        return self.name


class Toolbox:
    def __init__(self, tools):
        self.tools = tools

    def add(self, tool):
        self.tools.append(tool)

    def reduce(self, tool):
        if tool in self.tools:
            self.tools.remove(tool)
        else:
            print('工具箱没有这个工具')

    def search(self, tool):
        for t in self.tools:
            if tool == t:
                print(Tool.look(tool))

    def total(self):
        print('{}个'.format(len(self.tools)))
        pass


tool1 = Tool('铁锤', '锤铁钉', 20)
tool2 = Tool('胶钳', '夹东西', 15)
tool3 = Tool('螺丝刀', '拧螺丝', 10)
tool4 = Tool('钻头', '打洞', 12)
tool5 = Tool('电钻', '钻东西', 1000)
tool6 = Tool('剪刀', '剪东西', 8)
tool7 = Tool('线钳', '剪线', 25)
tool8 = Tool('螺丝', '固定物品', 5)

# 实例化对象
myToolBox = Toolbox([tool1])
# 添加工具
myToolBox.add(tool2)
print(myToolBox.tools)
myToolBox.add(tool3)
print(myToolBox.tools)
# 删除工具
myToolBox.reduce(tool2)
print(myToolBox.tools)
myToolBox.reduce(tool5)
print(myToolBox.tools)
# 查看工具
myToolBox.search(tool1)
# 工具总数
myToolBox.total()
