import pytest

from data.enter_class_data import test_data
from page.enter_class_page import enter_class_page

case_suite = test_data


@pytest.mark.usefixtures("init_enter_class_class")
@pytest.mark.enter
class TestEnter:
    """
    加入课堂测试用例
    """

    @pytest.mark.usefixtures("init_enter_class_function")
    @pytest.mark.parametrize("case_list", case_suite)
    def test_enter(self, case_list):

        # 进入课堂
        enter_class_page.execute_step(parameter=case_list["parameter"])

        # 获取断言
        actual_result = enter_class_page.assert_step(parameter=case_list["title"])

        expected_result = case_list["expected_result"]
        msg = case_list["title"]
        true_result = "pass"
        assert actual_result == expected_result
        print('{},执行结果为:{}'.format(msg, true_result))


if __name__ == "__main__":
    pytest.main()
