

import csv
import urllib
import ssl
from requests import Session
from requests.auth import HTTPBasicAuth

from np_helper import get_logger
from infs_np_client import infs_handle_np_request, infs_handle_np_request_cancel

from suds.client import Client
from suds.sax.element import Element
import suds.sax.attribute as attribute
from suds.plugin import MessagePlugin
from suds import WebFault

API_URL = "https://m2m.test.npcs.bh/services/NpcdbService?wsdl"
USERNAME = "soap_infs"
PASSWORD = "soap_infs"

logger = get_logger("CSYS_CLIENT_FOR_INFS")

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
            infs_resp = infs_handle_np_request(csys_resp)
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
            infs_resp = infs_handle_np_request_cancel(csys_resp)
        else:
            logger.error("CSYS SendNpRequestCancel Error:")
    except Exception as e:
        logger.error("CSYS SendNpRequestCancel Error: {}".format(str(e)))


def np_execute_from_INFS(client, request):

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
    logger.info(csys_resp)


def np_execute_complete_from_INFS(client, request):

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
    logger.info(csys_resp)
    infs_resp = infs_handle_np_execute_complete(csys_resp)
    logger.info(infs_resp)

if __name__ == "__main__":

    request = {
        "ServiceType" : "F",
        "MessageCode" : "NpRequest",
        "Number" : "16511870",
        "SubmissionID" : "INFX-2020-07060070",
        "DonorID" : "INFS",
        "RecipientID" : "INFX",
        "CompanyFlag" : "Y",
        "CPR" : "123456789",
        "CommercialRegNumber" : "12345/0",
        "Comments" : "NP Request",
        "OriginationID" : "INFX",
        "DestinationID" : "CSYS",
        "PortID" : "INFX-INFS-20200719-00024",
    }

    client = get_api()
    # print(client)
    # np_request_from_INFS(client, request)
    # np_request_cancel_from_INFS(client, request)
    np_execute_from_INFS(client, request)
