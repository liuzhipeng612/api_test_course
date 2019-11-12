import pytest

from data.join_class_data import test_data
from page.join_class_page import join_class_page

case_suite = test_data


@pytest.mark.usefixtures("init_join_class_class")
@pytest.mark.join
class TestJoin:
    """
    加入课堂测试用例
    """

    @pytest.mark.usefixtures("init_join_class_function")
    @pytest.mark.parametrize("case_list", case_suite)
    def test_join(self, case_list):
        # 加入课堂
        join_class_page.execute_step(parameter=case_list["parameter"])

        # 获取断言
        actual_result = join_class_page.assert_step(parameter=case_list["title"])

        expected_result = case_list["expected_result"]
        msg = case_list["title"]
        true_result = "pass"
        assert actual_result == expected_result
        print('{},执行结果为:{}'.format(msg, true_result))


if __name__ == "__main__":
    pytest.main()
