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