import pytest

from page.join_class_page import join_class_page
from page.enter_class_page import enter_class_page
from page.exit_class_page import exit_class_page


@pytest.fixture(scope="class")
def init_join_class_class():
    join_class_page.pre_step()
    yield
    join_class_page.post_step()
    join_class_page.quit()


@pytest.fixture(scope="function")
def init_join_class_function():
    join_class_page.function_pre_step()
    yield
    join_class_page.function_post_step()


@pytest.fixture(scope="class")
def init_enter_class_class():
    enter_class_page.pre_step()
    yield
    # enter_class_page.post_step()
    enter_class_page.quit()


@pytest.fixture(scope="function")
def init_enter_class_function():
    # enter_class_page.function_pre_step()
    yield
    enter_class_page.function_post_step()


@pytest.fixture(scope="class")
def init_exit_class_class():
    exit_class_page.pre_step()
    yield
    exit_class_page.quit()
