#!/usr/bin/env python
# coding=UTF-8
"""
@Author: Jomer
@Contact: jomer3126@gmail.com
@Project: Jomer
@File: test_cw0629_handle_config.py
@Time: 2019-07-05 01:48
@Desc: Jungle old monster
"""
from configparser import ConfigParser


class HandleConfig:
    """

    """

    def __init__(self, filename=None):
        self.filename = filename
        self.config = ConfigParser()
        self.config.read(self.filename, encoding='utf-8')

    def get_value(self, section, option):
        """

        :param section:
        :param option:
        :return:
        """
        return self.config.get(section, option)

    def get_int(self, section, option):
        """

        :param section:
        :param option:
        :return:
        """
        return self.config.getint(section, option)

    def get_float(self, section, option):
        """

        :param section:
        :param option:
        :return:
        """
        return self.config.getfloat(section, option)

    def get_boolean(self, section, option):
        """

        :param section:
        :param option:
        :return:
        """
        return self.config.getboolean(section, option)

    def get_eval_data(self, section, option):
        """

        :param section:
        :param option:
        :return:
        """
        return eval(self.get_value(section, option))

    @staticmethod
    def write_config(datas, filename):
        """

        :param data:
        :param filename:
        :return:
        """
        config = ConfigParser()
        for key in datas:
            config[key] = datas[key]

        # 3. 保存到文件
        with open(filename, 'w') as file:
            config.write(file)


do_config = HandleConfig("class_0629.conf")

if __name__ == '__main__':
    datas = {
        "file path": {'cases_path': 'cases.xlsx', 'log_path': 'record_run_result.txt'},
        "msg": {'success_result': 'Pass', 'fail_result': 'Fail'}
    }
    write_filename = "write_config2.ini"
    HandleConfig.write_config(datas, write_filename)
