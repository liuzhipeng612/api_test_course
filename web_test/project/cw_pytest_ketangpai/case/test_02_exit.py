import pytest

from data.exit_class_data import test_data
from page.exit_class_page import exit_class_page

case_suite = test_data


@pytest.mark.usefixtures("init_exit_class_class")
@pytest.mark.exit
class TestExit:
    """
    加入课堂测试用例
    """

    # @pytest.mark.usefixtures("init_exit_class_function")
    @pytest.mark.parametrize("case_list", case_suite)
    def test_exit(self, case_list):
        # 加入课堂
        exit_class_page.execute_step(parameter=case_list["parameter"])

        # 获取断言
        actual_result = exit_class_page.assert_step(parameter=case_list["title"])

        expected_result = case_list["expected_result"]
        msg = case_list["title"]
        true_result = "pass"
        assert actual_result == expected_result
        print('{},执行结果为:{}'.format(msg, true_result))


if __name__ == "__main__":
    pytest.main()
