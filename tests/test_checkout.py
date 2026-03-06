# tests/test_checkout.py

import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_e2e_shopping_flow(page):
    """
    核心业务链路测试：登录 -> 选商品加购 -> 进入购物车核对
    """
    # ================= 1. 登录模块 =================
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    
    # ================= 2. 商品列表模块 =================
    # 把同一个浏览器页面 page 传给下一个页面的对象
    inventory_page = InventoryPage(page)
    
    # 执行加购
    inventory_page.add_backpack_to_cart()
    
    # 【断言】：加购后，右上角的购物车红色数字应该变成 "1"
    expect(inventory_page.cart_badge).to_have_text("1")
    
    # 进入购物车
    inventory_page.go_to_cart()
    
    # ================= 3. 购物车模块核对 =================
    # 【断言】：验证是否成功跳转到了购物车页
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    # 【断言】：验证购物车里的商品名字对不对（没加错货吧？）
    expect(page.locator('.inventory_item_name')).to_have_text("Sauce Labs Backpack")