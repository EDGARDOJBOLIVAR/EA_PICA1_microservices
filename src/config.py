from decouple import config

class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = config('MYSQL_HOST')
    MYSQL_USER = config('MYSQL_USER')
    MYSQL_PORT = int(config('MYSQL_PORT'))
    MYSQL_PASSWORD = config('MYSQL_PASSWORD')
    MYSQL_DB = config('MYSQL_DB')
    SWAGGER_URL = config('SWAGGER_URL')
    API_URL = config('API_URL')

config = {
    'development': DevelopmentConfig
}