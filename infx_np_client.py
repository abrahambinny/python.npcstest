

import csv
import urllib
import ssl
from requests import Session
from requests.auth import HTTPBasicAuth
from np_helper import get_logger

from suds.client import Client
from suds.sax.element import Element
import suds.sax.attribute as attribute
from suds.plugin import MessagePlugin
from suds import WebFault

API_URL = "https://10.1.3.95:8005/spservice/service?wsdl"
USERNAME = "soap_csys_infx"
PASSWORD = "76Hu25ZPNJzJ2k2N"

logger = get_logger("INFX_CLIENT")

logger.info(API_URL)
logger.info(USERNAME)

def get_api():

    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context

    client = Client(API_URL, username=USERNAME, password=PASSWORD, headers = {'username': USERNAME, 'password': PASSWORD})
    client.set_options(location=API_URL, soapheaders=(USERNAME, PASSWORD))

    return client


def infx_handle_np_request(csys_resp):

    try:
        client = get_api()
        infs_resp = client.service.HandleNpRequest(
            ServiceType = csys_resp['ServiceType'],
            MessageCode = csys_resp['MessageCode'],
            Number = csys_resp['Number'],
            PortID = csys_resp['PortID'],
            SubmissionID = csys_resp['SubmissionID'],
            DonorID = csys_resp['DonorID'],
            RecipientID = csys_resp['RecipientID'],
            SimCardNumber = '',
            CompanyFlag = '',
            CPR = '',
            CommercialRegNumber = '',
            PassportNumber = '',
            GCCID = '',
            Comments = 'Response from csys',
            OriginationID = csys_resp['OriginationID'],
            DestinationID = csys_resp['DestinationID'],
        )
        if infs_resp:
            logger.info("INFX HandleNpRequest Response:")
            logger.info(infs_resp)
        else:
            logger.error("INFX HandleNpRequest Error:")
        return infs_resp
    except Exception as e:
        logger.error("INFX HandleNpRequest Error: {}".format(str(e)))


def infx_handle_np_request_cancel(csys_resp):

    try:
        client = get_api()
        infs_resp = client.service.HandleNpRequestCancel(
            ServiceType = csys_resp['ServiceType'],
            MessageCode = csys_resp['MessageCode'],
            PortID = csys_resp['PortID'],
            OriginationID = csys_resp['OriginationID'],
            DestinationID = csys_resp['DestinationID'],
            # Number = csys_resp['Number'],
            # SubmissionID = csys_resp['SubmissionID'],
            # DonorID = csys_resp['DonorID'],
            # RecipientID = csys_resp['RecipientID'],
        )
        if infs_resp:
            logger.info("INFX HandleNpRequestCancel Response:")
            logger.info(infs_resp)
        else:
            logger.error("INFX HandleNpRequestCancel Error:")
        return infs_resp
    except Exception as e:
        logger.error("INFX HandleNpRequestCancel Error: {}".format(str(e)))


def infx_handle_np_execute_broadcast(csys_resp):

    try:
        client = get_api()
        infs_resp = client.service.HandleNpExecuteBroadcast(
            ServiceType = csys_resp['ServiceType'],
            MessageCode = csys_resp['MessageCode'],
            Number = csys_resp['Number'],
            PortID = csys_resp['PortID'],
            DonorID = csys_resp['DonorID'],
            RecipientID = csys_resp['RecipientID'],
            NewRoute = csys_resp['NewRoute'],
            PortingDatetime = csys_resp['PortingDatetime'],
            OriginationID = csys_resp['OriginationID'],
            DestinationID = csys_resp['DestinationID'],
        )
        if infs_resp:
            logger.info("INFX HandleNpExecuteBroadcast Response:")
            logger.info(infs_resp)
        else:
            logger.error("INFX HandleNpExecuteBroadcast Error:")
        return infs_resp
    except Exception as e:
        logger.error("INFX HandleNpExecuteBroadcast Error: {}".format(str(e)))


def infx_handle_np_execute_complete(csys_resp):

    try:
        client = get_api()
        infx_resp = client.service.HandleNpExecuteComplete(
            ServiceType = csys_resp['ServiceType'],
            MessageCode = csys_resp['MessageCode'],
            PortID = csys_resp['PortID'],
            OriginationID = csys_resp['OriginationID'],
            DestinationID = csys_resp['DestinationID'],
            # Number = csys_resp['Number'],
            # SubmissionID = csys_resp['SubmissionID'],
            # DonorID = csys_resp['DonorID'],
            # RecipientID = csys_resp['RecipientID'],
        )
        if infx_resp:
            logger.info("infx HandleNpExecuteComplete Response:")
            logger.info(infx_resp)
        else:
            logger.error("INFX HandleNpExecuteComplete Error:")
        return infx_resp
    except Exception as e:
        logger.error("INFX HandleNpExecuteComplete Error: {}".format(str(e)))

def infx_handle_np_deactivate_complete(csys_resp):

    try:
        client = get_api()
        infx_resp = client.service.HandleNpDeactivateComplete(
            ServiceType = csys_resp['ServiceType'],
            MessageCode = csys_resp['MessageCode'],
            # Number = csys_resp['Number'],
            PortID = csys_resp['PortID'],
            # SubscriptionNetworkID = csys_resp['SubscriptionNetworkID'],
            # BlockID = csys_resp['BlockID'],
            OriginationID = csys_resp['OriginationID'],
            DestinationID = csys_resp['DestinationID'],
        )
        if infx_resp:
            logger.info("INFX HandleNpDeactivateComplete Response:")
            logger.info(infx_resp)
        else:
            logger.error("INFX HandleNpDeactivateComplete Error:")
        return infx_resp
    except Exception as e:
        logger.error("INFX HandleNpDeactivateComplete Error: {}".format(str(e)))


def infx_handle_np_query_complete(csys_resp):
    try:
        client = get_api()
        infx_resp = client.service.HandleNpQueryComplete(
            # ServiceType = csys_resp['ServiceType'],
            MessageCode = csys_resp['MessageCode'],
            Comments = "Np Query Complete",
            OriginationID = csys_resp['OriginationID'],
            DestinationID = csys_resp['DestinationID'],
        )
        logger.info("INFX HandleNpQueryComplete Response:")
        logger.info(infx_resp)
    except Exception as e:
        logger.error("INFX HandleNpQueryComplete Error: {}".format(str(e)))


def infx_handle_billing_resolution(csys_resp):

    try:
        client = get_api()
        infx_resp = client.service.HandleNpBillingResolution(
            ServiceType = csys_resp['ServiceType'],
            MessageCode = csys_resp['MessageCode'],
            # Number = csys_resp['Number'],
            PortID = csys_resp['PortID'],
            # DonorID = csys_resp['DonorID'],
            # SubscriptionNetworkID = csys_resp['SubscriptionNetworkID'],
            OriginationID = csys_resp['OriginationID'],
            DestinationID = csys_resp['DestinationID'],
        )
        logger.info("INFX HandleNpBillingResolution Response:")
        logger.info(infx_resp)
    except Exception as e:
        logger.error("INFX HandleNpBillingResolution Error: {}".format(str(e)))

def infx_handle_billing_resolution_end(csys_resp):

    try:
        client = get_api()
        infx_resp = client.service.HandleNpBillingResolutionEnd(
            ServiceType = csys_resp['ServiceType'],
            MessageCode = csys_resp['MessageCode'],
            # Number = csys_resp['Number'],
            PortID = csys_resp['PortID'],
            # DonorID = csys_resp['DonorID'],
            # SubscriptionNetworkID = csys_resp['SubscriptionNetworkID'],
            OriginationID = csys_resp['OriginationID'],
            DestinationID = csys_resp['DestinationID'],
        )
        logger.info("INFX HandleNpBillingResolutionEnd Response:")
        logger.info(infx_resp)
    except Exception as e:
        logger.error("INFX HandleNpBillingResolutionEnd Error: {}".format(str(e)))


if __name__ == "__main__":

    csys_resp = {
        "ServiceType" : "F",
        "MessageCode" : "MessageAck",
        "Number" : "16501825",
        "PortID" : "INFX-INFS-20200825-00002",
        "SubmissionID" : "INFX-2020-08250025",
        "DonorID" : "INFS",
        "RecipientID" : "INFX",
        "OriginationID" : "CSYS",
        "DestinationID" : "INFX",
        "NewRoute" : "a03",
        "PortingDatetime": "202007191242"
    }


    # infx_handle_np_request(csys_resp)
    # infx_handle_np_request_cancel(csys_resp)
    # infx_handle_np_execute_broadcast(csys_resp)
    # infx_handle_np_execute_complete(csys_resp)

    ### Deactivation
    csys_deactivate_resp = {
        "ServiceType" : "F",
        "MessageCode" : "NpDeactivateAck",
        "Number" : "16501825",
        "PortID" : "INFS-INFX-20200825-00003",
        "SubscriptionNetworkID" : "INFX",
        "BlockID" : "INFS",
        "OriginationID" : "CSYS",
        "DestinationID" : "INFX",
    }
    infx_handle_np_deactivate_complete(csys_deactivate_resp)

    ###Query
    csys_query_resp = {
        "ServiceType" : "F",
        "MessageCode" : "MessageAck",
        "PortID" : "NFS-CSYS-20200726-00013",
        "OriginationID" : "CSYS",
        "DestinationID" : "INFX",
    }
    # infx_handle_np_query_complete(csys_query_resp)

    ### Billing Resolution
    csys_billing_resp = {
        "ServiceType" : "F",
        "MessageCode" : "MessageAck",
        "PortID" : "INFX-INFS-20200727-00004",
        "OriginationID" : "CSYS",
        "DestinationID" : "INFS",
    }
    # infx_handle_billing_resolution(csys_resp)
    # infx_handle_billing_resolution_end(csys_resp)
