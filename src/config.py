class DevelopmentConfig():
    DEBUG=True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PORT = 33060
    MYSQL_PASSWORD = '123456'
    MYSQL_DB = 'mysql_docker'
    SWAGGER_URL = "/swagger"
    API_URL = "/static/swagger.json"

config = {
    'development': DevelopmentConfig
}