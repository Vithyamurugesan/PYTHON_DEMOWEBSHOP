import configparser
import os

class ReadConfig:
 
    def get_base_url():
        config = configparser.ConfigParser()
        config.read(os.path.join(os.path.dirname(__file__), "config.ini"))
        return config.get("common info", "baseURL")

    def get_email():
        config = configparser.ConfigParser()
        config.read(os.path.join(os.path.dirname(__file__), "config.ini"))
        return config.get("common info", "email")

    def get_password():
        config = configparser.ConfigParser()
        config.read(os.path.join(os.path.dirname(__file__), "config.ini"))
        return config.get("common info", "password")

    def get_browser():
        config = configparser.ConfigParser()
        config.read(os.path.join(os.path.dirname(__file__), "config.ini"))
        return config.get("browser", "browser")