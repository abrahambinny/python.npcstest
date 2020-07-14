

import csv
import urllib
import ssl
from requests import Session
from requests.auth import HTTPBasicAuth

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


def np_request_from_INFX():
    client = get_api()
    np_resp = client.service.SendNpRequest(
        ServiceType = "F",
        MessageCode = "NpRequest",
        Number = "16500001",
        PortID = "INFX-INFS-20180321-00043",
        SubmissionID = "INFX-2018-07060001",
        DonorID = "INFS",
        RecipientID = "INFX",
        # SimCardNumber = "",
        CompanyFlag = "Y",
        CPR = "123456789",
        CommercialRegNumber = "12345/0",
        # PassportNumber = "",
        # GCCID = "",
        Comments = "NP Request",
        OriginationID = "INFX",
        DestinationID = "CSYS"
    )
    print(np_resp)

if __name__ == "__main__":

    np_request_from_INFX()
