#!/usr/bin/env python
# coding=UTF-8
"""
@Author: Cautious Eureka
@Contact: Eureka@Faisen.com
@Project: cautious_eureka
@File: task0613.py
@Time: 2019-06-16 19:10
@Desc: Python full stack automation test engineer(Cautious Eureka)
"""
import random

"""
======必做题==========
1、使用思维导图总结梳理类与对象相关知识点
2：编程题
人和机器猜拳游戏写成一个类，有如下几个函数：
1）函数1：选择角色1 曹操 2张飞 3 刘备
2）函数2：角色猜拳1剪刀 2石头 3布 玩家输入一个1-3的数字
3）函数3：电脑出拳 随机产生1个1-3的数字，提示电脑出拳结果
4）函数4：角色和机器出拳对战，对战结束后，最后出示本局对战结果...赢...输,然后提示用户是否继续？按y继续，按n退出。
5）最后结束的时候输出结果 角色赢几局 电脑赢几局，平局几次 游戏结束
3、实现文字版游戏：坦克大战
步骤一：定义TANK类：
1、实现一个BaseTank类（所有Tank的父类）
BaseTank拥有live属性（这个属性代表Tank是否存活 :  1代表活的，0代表死）
BaseTank拥有postion属性（这个属性代表Tank的位置，位置随机生成，一共有（1,10）10个位置）
BeseTank拥有HP属性（代表血量，默认为10）
BeseTank拥有attck_postion属性（代表攻击位置，位置随机生成，一共有（1,10）10个位置）BeseTank拥有HP属性（代表血量，默认为10）
BaesTank拥有一个hit方法，该方法除self外，还接收一个参数other(代表对方Tank)，在该方法中判断，对方攻击位置和自己所在的位置是否一致，如果一致的话，就给自己的HP减1，当HP等于0时，修改live属性（改为死亡状态）
2、实现一个玩家坦克类，MyTank,继承于BaseTank，该类拥有两个方法。
move方法：(移动tank位置)调用该方法时，提示玩家输入移动的目标位置，输入完之后，将坦克移动到输入的位置，（输入无效数据，提示用户重新输入，通过异常来处理无效数据）
Bullet_launch方法：发射子弹，提示玩家输入攻击的目标位置，（输入无效数据，提示用户重新输入，通过异常来处理无效数据）
3、实现一个电脑坦克类，PCTank,继承于BaseTank，该类拥有两个方法。
move方法：(移动tank位置) 调用该方法时，随机移动位置（1,10）
Bullet_launch方法：发射子弹，攻击目标位置随机生成（1,10），
步骤二：选做题（扩展题，不要求提交）
2、游戏环节（循环，直到有tank死亡才退出循环）
1、玩家发生子弹，然后电脑坦克发射子弹，
2、玩家判断有没有被电脑击中，电脑判断有没有被玩家击中。
3、判断双方坦克是否存活，如果有tank死亡，则宣布存活的一方胜利。都存活则继续游戏。
4、玩家移动、电脑移动
"""

# 2：编程题
"""
人和机器猜拳游戏写成一个类，有如下几个函数：
1）函数1：选择角色1 曹操 2张飞 3 刘备 
2）函数2：角色猜拳1剪刀 2石头 3布 玩家输入一个1-3的数字
3）函数3：电脑出拳 随机产生1个1-3的数字，提示电脑出拳结果
4）函数4：角色和机器出拳对战，对战结束后，最后出示本局对战结果...赢...输,然后提示用户是否继续？按y继续，按n退出。
5）最后结束的时候输出结果 角色赢几局 电脑赢几局，平局几次 游戏结束
"""
"""
1、可选有三个角色中的一个作为输入项与电脑进行猜拳比赛
2、必选一个角色
3、角色只能选择1-3的数字
4、
"""


class Users:
    def __init__(self, user):
        self.user = user

    def add(self, serial, name):
        self.user[serial] = name


class Mora:
    def __init__(self, optional_role):
        self.optional_role = optional_role
        self.content_punch = {1: '剪刀', 2: '石头', 3: '布'}
        self.score_num = []
        self.score_name = []

    def role_selection(self, serial_number):
        """
        选择已有角色
        :param serial_number: 角色对应的号码
        :return: 返回角色的名称
        """
        for t in self.optional_role.keys():
            if serial_number == t:
                self.score_name.append(self.optional_role[serial_number])

    def role_punch(self, punch):
        """
        角色出拳
        :param punch: 角色出拳数字钟
        :return: 返回出拳数或错误状态
        """
        for p in self.content_punch.keys():
            if punch == p:
                self.score_num.append(punch)

    def robot_punch(self):
        """
        机器人出拳
        :return:
        """
        punch_num = random.randint(1, 3)
        for r in self.content_punch.keys():
            if punch_num == r:
                self.score_num.append(punch_num)
                self.score_name.append(self.content_punch[punch_num])

    def pk(self):
        if (self.score_num[0] < self.score_num[1] and self.score_num[1] - self.score_num[0] == 1) \
                or (self.score_num[0] > self.score_num[1] and self.score_num[1] - self.score_num[0] == -2):
            print("你赢了")
            self.score_name.append('赢')
        elif self.score_num[0] == self.score_num[1]:
            print("平局")
            self.score_name.append('平')
        else:
            print("你输了")
            self.score_name.append('输')

    @staticmethod
    def gap():
        print('\n\\\\', '*' * 69, '\n')

    def write(self):
        with open('score.txt', 'w+', encoding='utf-8')as score:
            winning = self.score_name.count('赢')
            draw = self.score_name.count('平')
            defeat = self.score_name.count('输')
            result = ['{}：{}赢，{}平，{}败'.format(self.score_name[0], winning, draw, defeat)]
            score.writelines(result)
            score.seek(0, 0)
            print(score.read())


# 初始化用户
role = Users({})
print(role)
# 添加用户
role.add(1, '曹操')
print(role.user)
role.add(2, '张飞')
print(role.user)
role.add(3, '刘备')
print(role.user)
Mora.gap()

# 实例化猜拳对象
my_mora = Mora(role.user)
# 选择角色
my_mora.role_selection(2)
while True:
    # 用户出拳
    punch_num = input("请出拳，1剪刀, 2石头, 3布")
    my_mora.role_punch(int(punch_num))
    # 电脑出拳
    my_mora.robot_punch()
    # 用户和电脑pk
    my_mora.pk()
    go = input("是否使用该角色继续猜拳，请输入‘y'或‘n’")
    if go == 'y':
        continue
    elif go == 'n':
        my_mora.write()
        break
    else:
        print('请正确输入选项')
        go = input("是否使用该角色继续猜拳，请输入‘y'或‘n’")
