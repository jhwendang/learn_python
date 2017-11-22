import settings
class MySQL:
    def __init__(self,host,port):
        self.host=host
        self.port=port

    @classmethod
    def from_conf(cls):
        return cls(settings.HOST,settings.PORT) #Mariadb('127.0.0.1',3306)
    # @staticmethod
    # def from_conf():
    #     return MySQL(settings.HOST, settings.PORT)  # MySQL('127.0.0.1',3306)
    def __str__(self):
        return '就不告诉你'
class Mariab(MySQL):
    def __str__(self):
        return 'host:%s port:%s' %(self.host,self.port)
    pass
conn1=Mariab.from_conf() #Mariadb('127.0.0.1',3306)
print(conn1)