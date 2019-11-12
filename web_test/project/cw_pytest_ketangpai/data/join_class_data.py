pre_step_data = [{
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

post_step_data = [{
    "step1": {
        "execute": "wait_visible_click",
        "locator": "css",
        "element": ".kdmore"
    }
}, {
    "step2": {
        "execute": "wait_visible_script_click",
        "locator": "css",
        "element": ".kdli3>a"
    }
}, {
    "step3": {
        "execute": "wait_visible_send_keys",
        "locator": "css",
        "element": ".deletekccon>input",
        "parameter": "yuangu2012"
    }
}, {
    "step4": {
        "execute": "wait_visible_click",
        "locator": "css",
        "element": ".dli2>a"
    }
}]

function_pre_step_data = [{
    "step1": {
        "execute": "wait_visible_click",
        "locator": "xpath",
        "element": "//div[@class='ktcon1l fr']"
    }
}]

function_post_step_data = [{"step1": {"execute": "wait_visible_click", "locator": "css", "element": ".cjli1>a"}}]

execute_step_data = [{
    "step1": {
        "execute": "wait_visible_send_keys",
        "locator": "css",
        "element": ".chuangjiankccon>input"
    }
}, {
    "step2": {
        "execute": "wait_visible_click",
        "locator": "css",
        "element": ".cjli2"
    }
}]

test_data = [{
    "title": "加课码不存在",
    "parameter": "123456",
    "expected_result": "该加课码不存在或者已经失效",
    "assert_step": {
        "execute": "wait_presence_text",
        "locator": "css",
        "element": "#error-tip>span"
    }
}, {
    "title": "验证码少于6位数",
    "parameter": "12345",
    "expected_result": "加课验证码必须是6位字符",
    "assert_step": {
        "execute": "wait_presence_text",
        "locator": "css",
        "element": "#error-tip>span"
    }
}, {
    "title": "已加入课堂",
    "parameter": "29942D",
    "expected_result": "你已经选过此课程",
    "assert_step": {
        "execute": "wait_presence_text",
        "locator": "css",
        "element": "#error-tip>span"
    }
}, {
    "title": "加课码为空",
    "parameter": "      ",
    "expected_result": "加课码不能为空",
    "assert_step": {
        "execute": "wait_presence_text",
        "locator": "css",
        "element": "#error-tip>span"
    }
}, {
    "title": "特殊符号",
    "parameter": "！@#￥%……",
    "expected_result": "该加课码不存在或者已经失效",
    "assert_step": {
        "execute": "wait_presence_text",
        "locator": "css",
        "element": "#error-tip>span"
    }
}, {
    "title": "正常加入",
    "parameter": "29942D",
    "expected_result": "加入课堂成功",
    "assert_step": {
        "execute": "wait_presence_text",
        "locator": "css",
        "element": ".gTips>span"
    }
}]
