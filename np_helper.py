
import logging
from np_config import *
from datetime import datetime

def get_logger(appname):
    today = datetime.today()
    log_file = '{}/log/{}_{}.log'.format(BASE_DIR, appname, datetime.strftime(today, "%Y-%m-%d"))

    logging.basicConfig(
        filename=log_file,
        # filemode='w',
        format='%(asctime)-15s - {} - %(levelname)s - %(message)s'.format(appname),level=logging.INFO
    )
    return logging


def suds_log(logger):

    logger.getLogger('suds.client').setLevel(logger.DEBUG)
    # logger.getLogger('suds.transport').setLevel(logger.DEBUG)
    # logger.getLogger('suds.xsd.schema').setLevel(logger.DEBUG)
    # logger.getLogger('suds.wsdl').setLevel(logger.DEBUG)
