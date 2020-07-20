

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

API_URL = "https://10.1.3.95:8000/spservice/service?wsdl"
USERNAME = "soap_csys_infs"
PASSWORD = "76Hu25ZPNJzJ2k2N"

logger = get_logger("INFS_CLIENT")

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


def infs_handle_np_request(csys_resp):

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
            logger.info("INFS HandleNpRequest Response:")
            logger.info(infs_resp)
        else:
            logger.error("INFS HandleNpRequest Error:")
        return infs_resp
    except Exception as e:
        logger.error("INFS HandleNpRequest Error: {}".format(str(e)))


def infs_handle_np_request_cancel(csys_resp):

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
            logger.info("INFS HandleNpRequestCancel Response:")
            logger.info(infs_resp)
        else:
            logger.error("INFS HandleNpRequestCancel Error:")
        return infs_resp
    except Exception as e:
        logger.error("INFS HandleNpRequestCancel Error: {}".format(str(e)))


def infs_handle_np_execute_broadcast(csys_resp):

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
            logger.info("INFS HandleNpExecuteBroadcast Response:")
            logger.info(infs_resp)
        else:
            logger.error("INFS HandleNpExecuteBroadcast Error:")
        return infs_resp
    except Exception as e:
        logger.error("INFS HandleNpExecuteBroadcast Error: {}".format(str(e)))


def infs_handle_np_execute_complete(csys_resp):

    try:
        client = get_api()
        infs_resp = client.service.HandleNpExecuteComplete(
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
            logger.info("INFS HandleNpExecuteComplete Response:")
            logger.info(infs_resp)
        else:
            logger.error("INFS HandleNpExecuteComplete Error:")
        return infs_resp
    except Exception as e:
        logger.error("INFS HandleNpExecuteComplete Error: {}".format(str(e)))


def infs_handle_np_deactivate_broadcast(csys_resp):

    try:
        client = get_api()
        infs_resp = client.service.HandleNpDeactivateBroadcast(
            ServiceType = csys_resp['ServiceType'],
            MessageCode = csys_resp['MessageCode'],
            Number = csys_resp['Number'],
            PortID = csys_resp['PortID'],
            SubscriptionNetworkID = csys_resp['SubscriptionNetworkID'],
            BlockID = csys_resp['SubscriptionNetworkID'],
            OriginationID = csys_resp['OriginationID'],
            DestinationID = csys_resp['DestinationID'],
        )
        if infs_resp:
            logger.info("INFS HandleNpDeactivateBroadcast Response:")
            logger.info(infs_resp)
        else:
            logger.error("INFS HandleNpDeactivateBroadcast Error:")
        return infs_resp
    except Exception as e:
        logger.error("INFS HandleNpDeactivateBroadcast Error: {}".format(str(e)))

def infs_handle_np_deactivate_complete(csys_resp):

    try:
        client = get_api()
        infs_resp = client.service.HandleNpDeactivateComplete(
            ServiceType = csys_resp['ServiceType'],
            MessageCode = "NpDeactivateComplete",
            Number = csys_resp['Number'],
            PortID = csys_resp['PortID'],
            SubscriptionNetworkID = csys_resp['SubscriptionNetworkID'],
            BlockID = csys_resp['BlockID'],
            OriginationID = csys_resp['OriginationID'],
            DestinationID = csys_resp['DestinationID'],
        )
        if infs_resp:
            logger.info("INFS HandleNpDeactivateComplete Response:")
            logger.info(infs_resp)
        else:
            logger.error("INFS HandleNpDeactivateComplete Error:")
        return infs_resp
    except Exception as e:
        logger.error("INFS HandleNpDeactivateComplete Error: {}".format(str(e)))


def infs_handle_np_query_complete(csys_resp):
    try:
        client = get_api()
        infs_resp = client.service.HandleNpQueryComplete(
            # ServiceType = csys_resp['ServiceType'],
            MessageCode = "NpQueryComplete",
            Comments = "Np Query Complete",
            OriginationID = csys_resp['OriginationID'],
            DestinationID = csys_resp['DestinationID'],
        )
        logger.info("INFS HandleNpQueryComplete Response:")
        logger.info(infs_resp)
    except Exception as e:
        logger.error("INFS HandleNpQueryComplete Error: {}".format(str(e)))

def infs_handle_billing_resolution_received(csys_resp):

    try:
        client = get_api()
        infx_resp = client.service.HandleNpBillingResolutionReceived(
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

if __name__ == "__main__":

    csys_resp = {
        "ServiceType" : "F",
        "MessageCode" : "MessageAck",
        "Number" : "16511870",
        "PortID" : "INFX-INFS-20200719-00024",
        "SubmissionID" : "INFX-2020-07060070",
        "DonorID" : "INFS",
        "RecipientID" : "INFX",
        "OriginationID" : "CSYS",
        "DestinationID" : "INFX",
        "NewRoute" : "a03",
        "PortingDatetime": "202007191242"
    }

    ### Preparation
    # infs_handle_np_request(client, csys_resp)
    # infs_handle_np_request_cancel(csys_resp)

    ### Execution
    # infs_handle_np_execute_broadcast(csys_resp)
    # infs_handle_np_execute_complete(csys_resp)

    ### Deactivation
    csys_deactivate_resp = {
        "ServiceType" : "F",
        "MessageCode" : "MessageAck",
        "Number" : "16511870",
        "PortID" : "INFS-INFX-20200719-00025",
        "SubscriptionNetworkID" : "INFX",
        "BlockID" : "INFS",
        "OriginationID" : "CSYS",
        "DestinationID" : "INFX",
    }
    # infs_handle_np_deactivate_complete(csys_deactivate_resp)

    ###Query
    csys_query_resp = {
        "ServiceType" : "F",
        "MessageCode" : "MessageAck",
        "PortID" : "INFX-CSYS-20200720-00000",
        "OriginationID" : "CSYS",
        "DestinationID" : "INFX",
    }
    # infs_handle_np_query_complete(csys_query_resp)

    ### Billing Resolution
    csys_billing_resp = {
        "ServiceType" : "F",
        "MessageCode" : "MessageAck",
        "PortID" : "INFX-INFS-20200719-00024",
        "OriginationID" : "CSYS",
        "DestinationID" : "INFX",
    }
    infs_handle_billing_resolution_received(csys_resp)
