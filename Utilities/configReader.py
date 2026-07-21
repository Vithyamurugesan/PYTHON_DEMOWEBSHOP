import configparser
import os

config = configparser.ConfigParser()

config_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "Configuration",
    "config.ini"
)

config.read(config_path)

print("Config Path:", config_path)
print("Sections:", config.sections())


class ReadConfig:

    @staticmethod
    def get_base_url():
        return config.get("common info", "baseURL")

    @staticmethod
    def get_email():
        return config.get("common info", "email")

    @staticmethod
    def get_password():
        return config.get("common info", "password")

    @staticmethod
    def get_browser():
        return config.get("common info", "browser")

    @staticmethod
    def get_compare_product():
        return config.get("compare info", "compare_product")

    @staticmethod
    def get_compare_product_two():
        return config.get("compare info", "compare_product_two")

    @staticmethod
    def get_empty_compare_msg():
        return config.get("compare info", "empty_compare_msg")

    @staticmethod
    def get_invalid_coupon_msg():
        return config.get("cart info", "invalid_coupon_msg")

    @staticmethod
    def get_empty_cart_msg():
        return config.get("cart info", "empty_cart_msg")

    @staticmethod
    def get_updated_quantity():
        return config.get("cart info", "updated_quantity")

    @staticmethod 
    def get_availability_label():
        return config.get("product detail info", "availability_label")

    @staticmethod
    def get_invalid_qty_msg():
        return config.get("product detail info", "invalid_qty_msg")

    @staticmethod
    def get_first_name():
        return config.get("empty_fields_test","first_name")

    @staticmethod
    def get_last_name():
        return config.get("empty_fields_test","last_name")

    @staticmethod
    def get_email_register():
        return config.get("empty_fields_test","email")

    @staticmethod  
    def get_password_required_error():
        return config.get("empty_fields_test","password_required")