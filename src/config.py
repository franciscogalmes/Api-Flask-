class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_DB = 'api_flask'
    MYSQL_PORT = 3306 

config = {
    'development': DevelopmentConfig
}