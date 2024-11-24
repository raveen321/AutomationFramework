import configparser

config=configparser.RawConfigParser()
config.read(".\\Cofiguration\\config.ini")

class readconfig():
    @staticmethod
    def getApplicationURL():
        url=config.get("common info","baseurl")
        return url

    @staticmethod
    def getUserName():
        username = config.get("common info", "username")
        return username


    @staticmethod
    def getPassword():
        password = config.get("common info", "password")
        return password