import time

from data.join_class_data import (test_data, post_step_data, pre_step_data, execute_step_data, function_post_step_data,
                                  function_pre_step_data)
from page.base_page import BasePage


class JoinClass(BasePage):
    """
    加入课堂page相关数据，自动获取对应的测试数据进行执行
    """

    # 解包
    @staticmethod
    def unpacking(args):
        return eval(str(args))

    @staticmethod
    def list_dict_de_weight(data=None):
        step_list = []
        for i in data:
            if i.keys() not in step_list:
                step_list.append(i)
        return step_list

    @staticmethod
    def dict_de_weight(data=None):
        step_list = []
        for i in data:
            if i["title"] not in step_list:
                step_list.append(i)
        return step_list

    def auto_execution_locator(self, data=None):
        """
        根据获得数据自动执行对应的定位方法
        :return:
        """
        for j in self.list_dict_de_weight(data):
            k = j.values()
            p = self.unpacking(*k)
            m = dict.copy(p)
            del m["execute"]
            eval("self." + p.get("execute", self.func_none))(**m)

    # class前置步骤
    def pre_step(self):
        """
        setUpClass步骤，由conftest调用
        :return:None
        """
        # 遍历执行一遍登录和跳转到课堂页面步骤
        self.auto_execution_locator(data=pre_step_data)

    # class后置步骤
    def post_step(self):
        """
        tearDownClass步骤，由conftest调用
        :return:None
        """
        # 遍历执行一遍退出课堂步骤
        self.auto_execution_locator(data=post_step_data)

    # function前置步骤
    def function_pre_step(self):
        """
        setUP步骤，由conftest调用
        :return: None
        """
        # 遍历执行一遍打开加入框步骤
        self.auto_execution_locator(data=function_pre_step_data)

    # function后置步骤
    def function_post_step(self):
        """
        tearDown步骤，由conftest调用
        :return:
        """
        # 遍历执行一遍退出加入框步骤
        self.auto_execution_locator(data=function_post_step_data)

    # 执行步骤
    def execute_step(self, parameter=None):
        """
        加入班级步骤
        :param parameter:
        :return: None
        """
        # 根据入参遍历执行一遍加入班级步骤
        for j in self.list_dict_de_weight(data=execute_step_data):
            k = j.values()
            p = self.unpacking(*k)
            m = dict.copy(p)
            del m["execute"]
            time.sleep(5)
            eval("self." + p.get("execute", self.func_none))(parameter=parameter, **m)

    # 断言步骤
    def assert_step(self, parameter=None):
        """
        获取正在被执行数据的断言
        :param parameter: 断言数据的标题名称
        :return: 将断言结果返回给pytest测试用例进行断言比较
        """
        # 获取正在被执行的测试数据
        assert_step_list = []
        for j in self.dict_de_weight(data=test_data):
            if j["title"] == parameter:
                assert_step_list.append(j)
        # 获取正在被执行的测试数据的断言数据
        for k in assert_step_list:
            m = k["assert_step"]
            n = dict.copy(m)
            del n["execute"]
            return eval("self." + m.get("execute", self.func_none))(**n)


join_class_page = JoinClass()

if __name__ == "__main__":
    aa = JoinClass()
    aa.pre_step()
    aa.execute_step(parameter="1234")
    pass
