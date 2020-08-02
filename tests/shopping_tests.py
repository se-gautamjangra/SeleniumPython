from selenium import webdriver
from page_objects.shopping_page import ShoppingPage
import pytest
import unittest
import os


class ShoppingTests(unittest.TestCase):
    dirname = os.getcwd()
    chrome_driver_path = dirname + '\\drivers\\chromedriver.exe'
    print('chrome path -> ' + chrome_driver_path)
    base_url = 'http://automationpractice.com/index.php'
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    driver.maximize_window()
    driver.implicitly_wait(5)
    # driver.get(base_url)
    driver.set_page_load_timeout(15)
    shopping_page = ShoppingPage(driver)
    product_name = 'Faded Short Sleeve T-shirts'

    @pytest.mark.run(order=0)
    def test_search_multiple_items(self):
        self.driver.get(self.base_url)
        self.shopping_page.search_item('Printed dress')
        self.shopping_page.submit_search()
        products_header = self.shopping_page.get_products_count()
        for header in products_header:
            print('element text -> ' + header.text)
            self.assertEqual(header.text, 'Showing 1 - 5 of 5 items')

    @pytest.mark.run(order=1)
    def test_search_single_item(self):
        # self.driver.get(self.base_url)
        self.shopping_page.search_item(self.product_name)
        self.shopping_page.submit_search()
        products_header = self.shopping_page.get_products_count()
        for header in products_header:
            print('element text -> ' + header.text)
            self.assertEqual(header.text, 'Showing 1 - 1 of 1 item')
        products = self.shopping_page.get_product_list()
        for ele in products:
            print('element text -> ' + ele.text)
            self.assertEqual(ele.text, self.product_name)

    @pytest.mark.run(order=2)
    def test_item_in_cart(self):
        self.shopping_page.select_item()
        self.shopping_page.proceed_to_checkout_dialog()
        cart_products = self.shopping_page.get_product_list_cart()
        for ele in cart_products:
            print('element text -> ' + ele.text)
            self.assertEqual(ele.text, self.product_name)

    @pytest.mark.run(order=3)
    def test_login_after_checkout(self):
        self.shopping_page.proceed_to_checkout_summary()
        self.assertTrue(self.shopping_page.is_login_present(), 'Login is present')
        self.assertTrue(self.shopping_page.is_create_account_present(), 'Create account is present')
        self.driver.close()
