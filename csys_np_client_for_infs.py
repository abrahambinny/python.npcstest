

import csv
import urllib
import ssl
from requests import Session
from requests.auth import HTTPBasicAuth

from np_helper import get_logger
from infx_np_client import *

from suds.client import Client
from suds.sax.element import Element
import suds.sax.attribute as attribute
from suds.plugin import MessagePlugin
from suds import WebFault

API_URL = "https://m2m.test.npcs.bh/services/NpcdbService?wsdl"
USERNAME = "soap_infs"
PASSWORD = "soap_infs"

logger = get_logger("CSYS_CLIENT_FOR_INFS")

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


def np_request_from_INFS(client, request):

    try:
        csys_resp = client.service.SendNpRequest(
            ServiceType = request['ServiceType'],
            MessageCode = "NpRequest",
            Number = request['Number'],
            SubmissionID = request['SubmissionID'],
            DonorID = request['DonorID'],
            RecipientID = request['RecipientID'],
            OriginationID = request['OriginationID'],
            DestinationID = request['DestinationID'],
            CompanyFlag = request['CompanyFlag'],
            CPR = request['CPR'],
            CommercialRegNumber = request['CommercialRegNumber'],
            Comments = request['Comments'],
            # PortID = "INFX-INFS-20200715-00002",
            # SimCardNumber = "",
            # PassportNumber = "",
            # GCCID = "",
        )
        if (csys_resp):
            logger.info("CSYS SendNpRequest Response:")
            logger.info(csys_resp)
            infx_resp = infx_handle_np_request(csys_resp)
        else:
            logger.error("CSYS SendNpRequest Error:")
    except Exception as e:
        logger.error("CSYS SendNpRequest Error: {}".format(str(e)))


def np_request_cancel_from_INFS(client, request):

    try:
        csys_resp = client.service.SendNpRequestCancel(
        ServiceType = request['ServiceType'],
            MessageCode = "NpRequestCancel",
            Number = request['Number'],
            SubmissionID = request['SubmissionID'],
            DonorID = request['DonorID'],
            RecipientID = request['RecipientID'],
            OriginationID = request['OriginationID'],
            DestinationID = request['DestinationID'],
            PortID = request['PortID'],
        )
        if csys_resp:
            logger.info("CSYS SendNpRequestCancel Response:")
            logger.info(csys_resp)
            infx_resp = infx_handle_np_request_cancel(csys_resp)
        else:
            logger.error("CSYS SendNpRequestCancel Error:")
    except Exception as e:
        logger.error("CSYS SendNpRequestCancel Error: {}".format(str(e)))


def np_execute_from_INFS(client, request):

    try:
        csys_resp = client.service.SendNpExecute(
            ServiceType = request['ServiceType'],
            MessageCode = "NpExecute",
            Number = request['Number'],
            PortID = request['PortID'],
            DonorID = request['DonorID'],
            RecipientID = request['RecipientID'],
            OriginationID = request['OriginationID'],
            DestinationID = request['DestinationID'],
        )
        if csys_resp:
            logger.info("CSYS SendNpExecute Response:")
            logger.info(csys_resp)
        else:
            logger.error("CSYS SendNpExecute Error:")
    except Exception as e:
        logger.error("CSYS SendNpExecute Error: {}".format(str(e)))


def np_execute_complete_from_INFS(client, request):

    try:
        csys_resp = client.service.SendNpExecuteComplete(
            ServiceType = request['ServiceType'],
            MessageCode = "NpExecuteComplete",
            Number = request['Number'],
            PortID = request['PortID'],
            DonorID = request['DonorID'],
            RecipientID = request['RecipientID'],
            OriginationID = request['OriginationID'],
            DestinationID = request['DestinationID'],
        )
        if csys_resp:
            logger.info("CSYS SendNpExecuteComplete Response:")
            logger.info(csys_resp)
            # infx_resp = infx_handle_np_execute_complete(csys_resp)
        else:
            logger.error("CSYS SendNpExecuteComplete Error:")
    except Exception as e:
        logger.error("CSYS SendNpExecuteComplete Error: {}".format(str(e)))

def np_deactivate_from_INFS(client, request):

    try:
        csys_resp = client.service.SendNpDeactivate(
            ServiceType = request['ServiceType'],
            MessageCode = "NpDeactivate",
            Number = request['Number'],
            SubscriptionNetworkID = request['SubscriptionNetworkID'],
            BlockID = request['BlockID'],
            OriginationID = request['OriginationID'],
            DestinationID = request['DestinationID'],
        )
        logger.info("CSYS NpDeactivate Response:")
        logger.info(csys_resp)
    except Exception as e:
        logger.error("CSYS NpDeactivate Error: {}".format(str(e)))

def np_deactivate_complete_from_INFS(client, request):

    try:
        csys_resp = client.service.SendNpDeactivateComplete(
            ServiceType = request['ServiceType'],
            MessageCode = "NpDeactivateComplete",
            Number = request['Number'],
            PortID = request['PortID'],
            SubscriptionNetworkID = request['SubscriptionNetworkID'],
            BlockID = request['BlockID'],
            OriginationID = request['OriginationID'],
            DestinationID = request['DestinationID'],
        )
        if csys_resp:
            logger.info("CSYS SendNpDeactivateComplete Response:")
            logger.info(csys_resp)
            infx_resp = infx_handle_np_deactivate_complete(csys_resp)
        else:
            logger.error("CSYS SendNpDeactivateComplete Error:")
    except Exception as e:
        logger.error("CSYS SendNpDeactivateComplete Error: {}".format(str(e)))

def np_query_from_INFS(client, request):

    try:
        csys_resp = client.service.SendNpQuery(
            MessageCode = "NpQuery",
            # DateFrom = request['DateFrom'],
            # DateTo = request['DateTo'],
            NumberFrom = request['NumberFrom'],
            NumberTo = request['NumberTo'],
            OperatorID = request['OperatorID'],
            Comments = request['Comments'],
            OriginationID = request['OriginationID'],
            DestinationID = request['DestinationID'],
        )
        logger.info("CSYS SendNpQuery Response:")
        logger.info(csys_resp)
    except Exception as e:
        logger.error("CSYS SendNpQuery Error: {}".format(str(e)))

def billing_resolution_from_INFS(client, request):

    try:
        csys_resp = client.service.SendNpBillingResolution(
            ServiceType = request['ServiceType'],
            MessageCode = "NpBillingResolution",
            Number = request['Number'],
            PortID = request['PortID'],
            DonorID = request['DonorID'],
            SubscriptionNetworkID = request['SubscriptionNetworkID'],
            OriginationID = request['OriginationID'],
            DestinationID = request['DestinationID'],
        )
        if csys_resp:
            logger.info("CSYS SendNpBillingResolution Response:")
            logger.info(csys_resp)
            infx_resp = infx_handle_billing_resolution(csys_resp)
        else:
            logger.error("CSYS SendNpBillingResolution Error:")
    except Exception as e:
        logger.error("CSYS SendNpBillingResolution Error: {}".format(str(e)))

def billing_resolution_end_from_INFS(client, request):

    try:
        csys_resp = client.service.SendNpBillingResolutionEnd(
            ServiceType = request['ServiceType'],
            MessageCode = "NpBillingResolutionEnd",
            Number = request['Number'],
            PortID = request['PortID'],
            DonorID = request['DonorID'],
            SubscriptionNetworkID = request['SubscriptionNetworkID'],
            OriginationID = request['OriginationID'],
            DestinationID = request['DestinationID'],
        )
        if csys_resp:
            logger.info("CSYS SendNpBillingResolutionEnd Response:")
            logger.info(csys_resp)
            infx_resp = infx_handle_billing_resolution_end(csys_resp)
        else:
            logger.error("CSYS SendNpBillingResolutionEnd Error:")
    except Exception as e:
        logger.error("CSYS SendNpBillingResolutionEnd Error: {}".format(str(e)))


if __name__ == "__main__":

    client = get_api()
    # print(client)

    request = {
        "ServiceType" : "F",
        "MessageCode" : "NpRequest",
        "Number" : "16511876",
        "SubmissionID" : "INFX-2020-07060076",
        "DonorID" : "INFS",
        "RecipientID" : "INFX",
        "CompanyFlag" : "Y",
        "CPR" : "123456789",
        "CommercialRegNumber" : "12345/0",
        "Comments" : "NP Request",
        "OriginationID" : "INFS",
        "DestinationID" : "CSYS",
        "PortID" : "INFX-INFS-20200727-00004",
    }

    ### Preparation
    # np_request_from_INFS(client, request)
    # np_request_cancel_from_INFS(client, request)

    ### Execution
    # np_execute_from_INFS(client, request)
    # np_execute_complete_from_INFS(client, request)

    ### Deactivation
    request_deactivate = {
        "ServiceType" : "F",
        "MessageCode" : "NpDeactivate",
        "Number" : "16511874",
        "PortID" : "INFS-INFX-20200726-00012",
        "SubscriptionNetworkID" : "INFX",
        "BlockID" : "INFS",
        "OriginationID" : "INFS",
        "DestinationID" : "CSYS",
    }
    # np_deactivate_from_INFS(client, request_deactivate)
    # np_deactivate_complete_from_INFS(client, request_deactivate)

    ### Query
    request_query =  {
        "MessageCode" : "NpQuery",
        "DateFrom" : "202007190000",
        "DateTo" : "202007220000",
        "NumberFrom" : "16511860",
        "NumberTo" : "16511880",
        "OperatorID": "INFX",
        "Comments": "NP Query",
        "OriginationID" : "INFS",
        "DestinationID" : "CSYS",
    }
    # np_query_from_INFS(client, request_query)

    ### Billing Resolution Process

    request_billing_resolution = {
        "ServiceType" : "F",
        "MessageCode" : "NpBillingResolution”",
        "Number" : "16511876",
        "PortID" : "INFX-INFS-20200727-00004",
        "SubscriptionNetworkID" : "INFX",
        "DonorID" : "INFS",
        "OriginationID" : "INFS",
        "DestinationID" : "CSYS",
    }
    # billing_resolution_from_INFS(client, request_billing_resolution)
    # billing_resolution_end_from_INFS(client, request_billing_resolution)
