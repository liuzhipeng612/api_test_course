import random

# 1.在异常中，try关键字下的块语句、except下的块语句、else下的块语句、finally下的块语句执行逻辑是什么？
"""
答：
    try关键字下的块语句：对代码进行校验测试
    except下的块语句：如果try中代码出现异常，会启用except模块下的代码，如果已知异常类型，可对相应异常作专一处理
    else下的块语句：如果try中代码正常执行，else模块下的代码会接着执行，该代码不做异常检测
    finally下的块语句：如果try中的代码出现异常，finally中的代码会被执行，保证其他代码不受try中异常影响造成崩溃
"""
# 2.编写如下程序
# 优化去生鲜超市买橘子程序
# a.收银员输入橘子的价格，单位：元／斤
# b.收银员输入用户购买橘子的重量，单位：斤
# c.计算并且 输出 付款金额
# 新需求：
# d.使用捕获异常的方式，来处理用户输入无效数据的情况
try:
    while True:
        price = input("Please input price: ")
        quantity = input("Please input quantity: ")
        money = int(price) * int(quantity)
        print("用户购买了{}斤，{}元/斤的橘子，总价{}元".format(price, quantity, money))
except ValueError:
    print('输入异常，请输入整数：')

# 3.编写如下程序
# 优化剪刀石头布游戏程序
# a.提示用户输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
# b.电脑随机出拳
# c.比较胜负，显示用户胜、负还是平局
# 新需求：
# d.使用捕获异常的方式，来处理用户输入无效数据的情况
# e.多次进行游戏，可以让用户选择退出游戏，退出后需要显示胜利情况，例如：用户5局胜、3局败、2局平
# f.当程序结束之后，要求下一次运行程序能够获取用户历史胜负情况
# h.如果使用文件保存用户历史胜负数据，需要使用异常来处理文件不存在的情况和实现程序结束后自动关闭文件的功能（选做）
try:
    with open('statisticalFile.txt', 'r+', encoding='utf-8') as statisticalFile1:
        print('上次战况：' + statisticalFile1.read())
    battleStatistics = []
    while True:
        punch = input("请出拳：")
        punch = int(punch)
        robot = random.randint(0, 3)
        if punch in range(4):
            if punch == 0:
                winning = battleStatistics.count('胜局')
                draw = battleStatistics.count('平局')
                defeat = battleStatistics.count('败局')
                result = ['用户{}胜局，{}平局，{}败局'.format(winning, draw, defeat)]
                with open('statisticalFile.txt', 'w+', encoding='utf-8') as statisticalFile2:
                    statisticalFile2.writelines(result)
                    statisticalFile2.seek(0, 0)
                    print(statisticalFile2.read())
                break
            elif (punch < robot and robot - punch == 1) \
                    or (punch > robot and robot - punch == -2):
                print("你赢了")
                battleStatistics.append('胜局')
            elif punch == robot:
                print("平局")
                battleStatistics.append('平局')
            else:
                print("你输了")
                battleStatistics.append('败局')
except ValueError:
    print('输入异常，只能输入数字0，1，2，3，请重新输入')
