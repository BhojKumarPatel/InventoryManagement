from Abstractions.Products import Products
from Models.ProductModel import ProductModel
from Models.VendorSessionModel import VendorSessionModel


class ProductsImplementation(Products):

    def __init__(self, username):
        self.product_model = ProductModel()
        self.vendor_session = VendorSessionModel()
        self._username = username

    def add_product(self, product_name, product_type, available_quantity, unit_price):
        # check if the vendor is logged in, then add the product and return True else Return False
        if not self.vendor_session.check_login(self._username):
            print("Not Authorized Vendor")
            return False
        else:
            product_add = self.product_model.add_product(product_name, product_type, available_quantity,
                                                         unit_price)
            if product_add:
                print("Product Added successfully")
                return True
            else:
                print("Product Addition Failed")
                return False
            
    def search_product_by_name(self, product_name):
        # Search if the product is available in the dictionary if the vendor is authorized to access else return False
        # If product is available then return product
        if not self.vendor_session.check_login(self._username):
            print("Not Authorized Vendor")
            return False
        else:
            #print("\n Searching for product {}\n".format(product_name))
            product = self.product_model.search_product(product_name)
            return product

    def get_all_products(self):
        # Check if the vendor can retrieve all the product if not return False
        # otherwise return all the products
        if not self.vendor_session.check_login(self._username):
            print("Not Authorized Vendor")
            return False
        else:
            #print("\n Getting all products for: {}\n".format(self._username))
            all_products = self.product_model.all_products()
            return all_products

