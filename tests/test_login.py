# tests/test_login.py

import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage

def test_standard_user_login_success(page):
    """
    测试用例：正常用户成功登录电商系统
    """
    # 1. 实例化页面对象 (剥离了底层定位逻辑，用例代码变得极其易读！)
    login_page = LoginPage(page)
    
    # 2. 执行测试步骤
    login_page.navigate()
    # "standard_user" 和 "secret_sauce" 是该靶场提供的合法测试账号
    login_page.login("standard_user", "secret_sauce")
    
    # 3. 核心断言 (Assert)
    # UI 测试不仅仅是点通了就行，必须验证页面是否真的跳转了，特定元素是否出现了
    
    # 断言一：URL 是否成功跳转到了商品列表页 (inventory.html)
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    
    # 断言二：页面左上角是否出现了 "Products" 这个标题文字
    # .title 是那个文字的 CSS class 属性
    expect(page.locator(".title")).to_have_text("Super Products")


# ================= 新增：使用 DDT 数据驱动测试异常登录 =================

# 这就是数据驱动的魔法！我们定义了 3 组异常数据。
# 每组数据包含 3 个参数：账号、密码、预期出现的报错信息
@pytest.mark.parametrize("username, password, expected_error",[
    ("locked_out_user", "secret_sauce", "Sorry, this user has been locked out."),
    ("standard_user", "wrong_password", "Username and password do not match any user in this service"),
    ("", "secret_sauce", "Username is required"),
])
def test_abnormal_login(page, username, password, expected_error):
    """
    测试用例：数据驱动的异常登录场景
    """
    login_page = LoginPage(page)
    login_page.navigate()
    
    # 这里的账号和密码，是从上面的 @pytest.mark.parametrize 里自动传进来的！
    login_page.login(username, password)
    
    # 【断言】：SauceDemo 的错误提示框的定位器是 [data-test="error"]
    error_message_box = page.locator('[data-test="error"]')
    
    # 我们期望这个错误提示框里，包含我们预先写好的 expected_error 文字
    # to_contain_text 比 to_have_text 更灵活，它是模糊匹配（包含即可）
    expect(error_message_box).to_contain_text(expected_error)