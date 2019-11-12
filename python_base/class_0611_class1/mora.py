#!/usr/bin/env python
# coding=UTF-8
"""
@Author: Cautious Eureka
@Contact: Eureka@Faisen.com
@Project: cautious_eureka
@File: mora.py
@Time: 2019-06-16 23:48
@Desc: Python full stack automation test engineer(Cautious Eureka)
"""


class Users:
    def __init__(self, user):
        self.user = user

    def add(self, serial, name):
        self.user.append(serial)
        self.user.append(name)

    # def __repr__(self):
    #     return self.user


class Mora:
    def __init__(self, optional_role):
        self.optional_role = optional_role

    # def role_selection(self, serial_number):
    #     for t in self.optional_role:
    #         if serial_number == t:
    #             print(serial_number)
    def search(self, tool):
        for t in self.optional_role:
            if tool == t:
                print('q')

    @staticmethod
    def gap():
        print('\n\\\\', '*' * 69, '\n')


role = Users([0, '曹操0'])
print(role)
role.add(1, '曹操')
print(type(role.user))
role.add(2, '张飞')
print(role.user)
role.add(3, '刘备')
print(role.user)

my_mora = Mora(role.user)
print(my_mora)
print(my_mora.search(1))
