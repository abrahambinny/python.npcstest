
from config.dev import config as dev_config
from config.prod import config as prod_config
import os,sys

environment = os.environ['APP_ENV'] or 'dev'
environment_config = None
if environment == 'dev':
    environment_config = dev_config
if environment == 'prod':
    environment_config = prod_config
