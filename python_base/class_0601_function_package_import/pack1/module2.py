# #1    from ... import ... 调用：函数
# from module1 import mod1 as mod
#
# mod()
# ############

# #2
# from module1 import mod1
#
# mod1()
# #############

# #3
# from module1 import *
#
# mod1()
# #############

# #4    import ... 调用：模板名.函数
# import module1
#
# module1.mod1()
# ############

# #5
# import module1 as mod
#
# mod.mod1()
# ##############

##模块在同一包里面：可以使用from ... import ...
##模块与包同级:可以使用from ... import ...
##同级包里面的模块调用

# from 模板相对路径 import 函数
# import 模板相对路径
