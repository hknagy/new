
class BaseConfig(object):
   DEBUG = False


class TestConfig(BaseConfig):
   DEBUG = True
   TESTING = True

class DevelopmentConfig(BaseConfig):
   DEBUG = True

class ProductionConfig(BaseConfig):
   DEBUG = False
