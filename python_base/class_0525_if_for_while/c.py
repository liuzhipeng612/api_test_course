#!/usr/bin/env python
# coding=UTF-8
"""
@Author: Cautious Eureka
@Contact: Eureka@Faisen.com
@Project: cautious_eureka
@File: c.py
@Time: 2019/5/22 1:39
@Desc: Python full stack automation test engineer(Cautious Eureka)
"""

# import os
#
# dict = {'223.104.24.119': set(['006534']), '182.97.184.36': set(['006667']),
#         '101.90.127.199': set(['002171']), '223.104.20.68': set(['002392']),
#         '117.165.41.31': set(['002584', '002411', '013489', '002456']),
#         '124.236.129.138': set(['001002']),
#         '117.136.79.117': set(['017495']), '223.104.63.226': set(['003168'])}
#
# write_file = os.getcwd() + '/dit.txt'
#
# print(write_file)
# output = open(write_file, 'w')
# for i in dict:
#     print(i, dict[i])
#     print(list(dict[i]))
#
#
#     output.write(str(i))
#     output.write('')
#     output.write(str(list(dict[i])))
#     output.write('\n')
#     # write_str = str(i) + '' + str(list(dict[i])) + '\n'
#     # output.write(write_str)
with open('dit.txt')as dit:
    print(dit.read())
    print(type(dit.read()))
