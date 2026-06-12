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


    def get_base_url():
        return config.get("common info", "baseURL")

    def get_email():
        return config.get("common info", "email")

    def get_password():
        return config.get("common info", "password")

    def get_browser():
        return config.get("common info", "browser")

    def get_invalid_coupon_msg():
        return config.get("cart info", "invalid_coupon_msg")

   
    def get_empty_cart_msg():
        return config.get("cart info", "empty_cart_msg")


    def get_updated_quantity():
        return config.get("cart info", "updated_quantity")

  
    def get_availability_label():
        return config.get("product detail info", "availability_label")


    def get_invalid_qty_msg():
        return config.get("product detail info", "invalid_qty_msg")
    
    def get_first_name():
        return config.get("empty_fields_test","first_name")
    
    def get_last_name():
        return config.get("empty_fields_test","last_name")

    def get_email():
        return config.get("empty_fields_test","email")
    
    def get_password_required_error():
        return config.get("empty_fields_test","password_required")