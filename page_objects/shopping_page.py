from utilities.web_utils import SeleniumDriver


class ShoppingPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _search_box = 'search_query_top'
    _search_submit = 'submit_search'
    _search_products_count = '//div[@class="product-count"]'
    _searched_items = '//a[@class="product_img_link"]/img'
    _product_list = '//ul[@class="product_list grid row"]//a[@class="product-name"]'
    _add_to_cart = '//a[@title="Add to cart"]/span'
    _view_cart = '//a[@title="View my shopping cart"]/span'
    _cart_items = '//a[@class="cart_block_product_name"]'
    _dialog_proceed_to_checkout = '//a[@title="Proceed to checkout"]'
    _dialog_continue_shopping = '//span[@title="Continue shopping"]'
    _summary_proceed_to_checkout = '//p[@class="cart_navigation clearfix"]//a[@title="Proceed to checkout"]'
    _cart_product_list = '//table[@id="cart_summary"]//p[@class="product-name"]//a'
    _create_account = 'SubmitCreate'
    _login_account = 'SubmitLogin'

    def search_item(self, item):
        self.set_text(item, self._search_box, locator_type="id")

    def submit_search(self):
        self.click_element(self._search_submit, locator_type="name")

    def get_products_count(self):
        elements = self.get_elements(self._search_products_count, locator_type="xpath")
        return elements

    def select_item(self):
        self.scroll_to_element_view(self._search_products_count, locator_type="xpath")
        self.perform_hover(self._product_list, locator_type="xpath")
        self.javascript_click(self._add_to_cart, locator_type='xpath')

    def get_product_list(self):
        elements = self.get_elements(self._product_list, locator_type="xpath")
        return elements

    def continue_shopping_dialog(self):
        self.click_element(self._dialog_continue_shopping, locator_type='xpath')

    def proceed_to_checkout_dialog(self):
        self.click_element(self._dialog_proceed_to_checkout, locator_type='xpath')

    def proceed_to_checkout_summary(self):
        self.click_element(self._summary_proceed_to_checkout, locator_type='xpath')

    def get_product_list_cart(self):
        elements = self.get_elements(self._cart_product_list, locator_type="xpath")
        return elements

    def is_login_present(self):
        return self.is_element_present(self._login_account,locator_type='id')

    def is_create_account_present(self):
        return self.is_element_present(self._create_account,locator_type='id')