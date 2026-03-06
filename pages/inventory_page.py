# pages/inventory_page.py

class InventoryPage:
    def __init__(self, page):
        self.page = page
        # 定位“加入购物车”按钮 (针对特定的背包商品)
        self.add_backpack_btn = page.locator('[data-test="add-to-cart-sauce-labs-backpack"]')
        # 定位右上角的购物车图标
        self.cart_link = page.locator('.shopping_cart_link')
        # 定位购物车图标上的红色数字角标
        self.cart_badge = page.locator('.shopping_cart_badge')

    def add_backpack_to_cart(self):
        """业务动作：将背包加入购物车"""
        self.add_backpack_btn.click()

    def go_to_cart(self):
        """业务动作：点击右上角进入购物车页面"""
        self.cart_link.click()