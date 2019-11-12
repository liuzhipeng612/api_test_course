from typing import Dict, List, Union

# setUpClass数据，登录并进入课堂页面
pre_step_data: List[Dict[str, Dict[str, str]]] = [{
    "step1": {
        "execute": "open_url",
        "parameter": "https://www.ketangpai.com/Home/User/login.html"
    }
}, {
    "step2": {
        "execute": "wait_visible_send_keys",
        "locator": "xpath",
        "element": "//input[@placeholder='邮箱/账号/手机号']",
        "parameter": "jomer3126@gmail.com"
    }
}, {
    "step3": {
        "execute": "wait_visible_send_keys",
        "locator": "xpath",
        "element": "//input[@type='password']",
        "parameter": "yuangu2012"
    }
}, {
    "step4": {
        "execute": "wait_visible_click",
        "locator": "xpath",
        "element": "//div[@class='padding-cont pt-login']//a[@class='btn-btn']"
    }
}]

# setUp数据，打开加入课堂模块并加入
function_pre_step_data: List[Dict[str, Dict[str, str]]] = [{
    "step1": {
        "execute": "wait_visible_click",
        "locator": "xpath",
        "element": "//div[@class='ktcon1l fr']"
    }
}, {
    "step2": {
        "execute": "wait_visible_send_keys",
        "locator": "css",
        "element": ".chuangjiankccon>input",
        "parameter": "29942D"
    }
}, {
    "step3": {
        "execute": "wait_visible_click",
        "locator": "css",
        "element": ".cjli2"
    }
}]

# 执行退出课堂数据
execute_step_data: List[Dict[str, Dict[str, str]]] = [{
    "step1": {
        "execute": "wait_visible_click",
        "locator": "css",
        "element": ".bgclass0 .kdmore"
    }
}, {
    "step2": {
        "execute": "wait_visible_script_click",
        "locator": "css",
        "element": ".bgclass0 .kdli3>a"
    }
}, {
    "step3": {
        "execute": "wait_visible_send_keys",
        "locator": "css",
        "element": ".deletekccon>input"
    }
}, {
    "step4": {
        "execute": "wait_visible_click",
        "locator": "css",
        "element": ".dli2>a"
    }
}]

test_data: List[Dict[str, Union[str, Dict[str, str]]]] = [{
    "title": "限制退出课堂",
    "parameter": "yuangu2012",
    "expected_result": "老师不允许学生进行退课，如需要退课，请找老师进行删除",
    "assert_step": {
        "execute": "wait_presence_text",
        "locator": "css",
        "element": "#error-tip>span"
    }
}]
