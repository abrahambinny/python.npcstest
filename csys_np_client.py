

import csv
import urllib
import ssl
from requests import Session
from requests.auth import HTTPBasicAuth

from infs_np_client import *
from infx_np_client import *

from suds.client import Client
from suds.sax.element import Element
import suds.sax.attribute as attribute
from suds.plugin import MessagePlugin
from suds import WebFault

API_URL = "https://m2m.test.npcs.bh/services/NpcdbService?wsdl"
USERNAME = "soap_infx"
PASSWORD = "soap_infx"

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


def np_request_from_INFX(client, request):

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
    infs_resp = infs_handle_np_request(csys_resp)
    print(infs_resp)


def np_request_cancel_from_INFX(client, request):

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
    print(csys_resp)
    infs_handle_np_request_cancel(client, csys_resp)

if __name__ == "__main__":

    request = {
        "ServiceType" : "F",
        "MessageCode" : "NpRequest",
        "Number" : "16511861",
        "SubmissionID" : "INFX-2020-07060061",
        "DonorID" : "INFS",
        "RecipientID" : "INFX",
        "CompanyFlag" : "Y",
        "CPR" : "123456789",
        "CommercialRegNumber" : "12345/0",
        "Comments" : "NP Request",
        "OriginationID" : "INFX",
        "DestinationID" : "CSYS",
        "PortID" : "INFX-INFS-20200716-00014",
    }

    client = get_api()
    print(client)
    # np_request_from_INFX(client, request)
    # np_request_cancel_from_INFX(client, request)
