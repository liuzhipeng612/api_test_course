#!/usr/bin/env python
# coding=UTF-8
"""
@Author: Cautious Eureka
@Contact: Eureka@Faisen.com
@Project: cautious_eureka
@File: handle_path.py
@Time: 2019-08-02 22:35
@Desc: Eureka
"""
import os
from datetime import datetime


class HandlePath:
    """
    处理文件路径，供个模块调用
    """
    pass


# 获取根目录
# one_path=os.path.abspath(__file__)
# two_path=os.path.dirname(one_path)
# three_path=os.path.dirname(two_path)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 获取测试用例CASE目录
CASE_DIR = os.path.join(BASE_DIR, 'case')
CASE_TEST_01_REGISTER_FILE_PATH = os.path.join(CASE_DIR, 'test_01_register.py')

# 获取配置文件CONFIG目录
CONFIG_DIR = os.path.join(BASE_DIR, 'config')
CONFIG_BASE_FILE_PATH = os.path.join(CONFIG_DIR, 'base.conf')
CONFIG_WRITE_CONFIG_FILE_PATH = os.path.join(CONFIG_DIR, 'write_config.ini')

# 获取测试数据DATA目录
DATA_DIR = os.path.join(BASE_DIR, 'data')
DATA_COMMON_FILE_PATH = os.path.join(DATA_DIR, 'common.xlsx')

# 获取第三方库文件LIBRARY目录
LIBRARY_DIR = os.path.join(BASE_DIR, 'library')
LIBRARY_DDT_FILE_PATH = os.path.join(LIBRARY_DIR, 'ddt.py')
LIBRARY_TEST_RUNNER_FILE_PATH = os.path.join(LIBRARY_DIR, 'HTMLTestRunnerNew.py')

# 获取日志文件LOG目录
LOG_DIR = os.path.join(BASE_DIR, 'log')
LOG_DEBUG_FILE_PATH = os.path.join(LOG_DIR, 'debug.log')
LOG_INFO_FILE_PATH = os.path.join(LOG_DIR, 'info.log')
LOG_WARNING_FILE_PATH = os.path.join(LOG_DIR, 'warning.log')
LOG_ERROR_FILE_PATH = os.path.join(LOG_DIR, 'error.log')
LOG_CRITICAL_FILE_PATH = os.path.join(LOG_DIR, 'critical.log')
LOG_RUN_RECORD_FILE_PATH = os.path.join(LOG_DIR, 'run_record.txt')

# 获取获取测试报告reports目录
REPORT_DIR = os.path.join(BASE_DIR, 'report')
report_name_prefix = 'test_reports_'
report_name_suffix = '.html'
report_name_time = datetime.strftime(datetime.now(), '%Y%m%d_%H%M%S')
report_name = report_name_prefix + report_name_time + report_name_suffix
REPORT_FILE_PATH = os.path.join(REPORT_DIR, report_name)

# 获取脚本封装scripts目录
SCRIPT_DIR = os.path.join(BASE_DIR, 'script')
HANDLE_CONFIG_FILE_PATH = os.path.join(SCRIPT_DIR, 'handle_config.py')
HANDLE_CONTEXT_FILE_PATH = os.path.join(SCRIPT_DIR, 'handle_context.py')
HANDLE_EXCEL_FILE_PATH = os.path.join(SCRIPT_DIR, 'handle_excel.py')
HANDLE_TEST_EXCEL_FILE_PATH = os.path.join(SCRIPT_DIR, 'test_handle_excel.py')
HANDLE_LOG_FILE_PATH = os.path.join(SCRIPT_DIR, 'handle_log.py')
HANDLE_MYSQL_FILE_PATH = os.path.join(SCRIPT_DIR, 'handle_mysql.py')
HANDLE_REGISTER_FILE_PATH = os.path.join(SCRIPT_DIR, 'handle_register.py')
HANDLE_REQUEST_FILE_PATH = os.path.join(SCRIPT_DIR, 'handle_request.py')
HANDLE_SUITE_FILE_PATH = os.path.join(SCRIPT_DIR, 'handle_test_suite.py')

# 获取临时测试test目录
TEST_DIR = os.path.join(BASE_DIR, 'test')

if __name__ == "__main__":
    print('获取项目根目录：')
    print(PROJECT_DIR)

    print('基本模块目录：')
    print(BASE_DIR)
    print(CASE_DIR)
    print(CONFIG_DIR)
    print(DATA_DIR)
    print(LIBRARY_DIR)
    print(LOG_DIR)
    print(REPORT_DIR)
    print(SCRIPT_DIR)

    print('文件路径：')
    print(CASE_TEST_01_REGISTER_FILE_PATH)
    print(CONFIG_BASE_FILE_PATH)
    print(CONFIG_WRITE_CONFIG_FILE_PATH)
    print(DATA_COMMON_FILE_PATH)
    print(LIBRARY_DDT_FILE_PATH)
    print(LIBRARY_TEST_RUNNER_FILE_PATH)
    print(LOG_DEBUG_FILE_PATH)
    print(REPORT_FILE_PATH)
    print(HANDLE_CONFIG_FILE_PATH)
    print(HANDLE_CONTEXT_FILE_PATH)
    print(HANDLE_EXCEL_FILE_PATH)
    print(HANDLE_LOG_FILE_PATH)
    print(HANDLE_MYSQL_FILE_PATH)
    print(HANDLE_REGISTER_FILE_PATH)
    print(HANDLE_REQUEST_FILE_PATH)
    print(HANDLE_SUITE_FILE_PATH)
