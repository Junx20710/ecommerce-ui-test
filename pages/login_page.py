# pages/login_page.py

class LoginPage:
    """
    登录页面的 Page Object 类
    封装了该页面所有的元素定位和业务操作
    """
    def __init__(self, page):
        # 接收 Playwright 的 page 对象
        self.page = page
        
        # 【核心考点：元素定位】
        # Playwright 强烈推荐使用具备唯一业务属性的属性来定位，比如 data-test
        # 这比老旧的 xpath 稳定一万倍，前端改了排版也不会报错！
        self.username_input = page.locator("[data-test='username']")
        self.password_input = page.locator("[data-test='password']")
        self.login_button = page.locator("[data-test='login-button']")

    def navigate(self):
        """打开登录页面"""
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username, password):
        """执行登录动作的业务流"""
        # Playwright 的 .fill() 会自带自动等待机制，等元素可见了才会输入
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()