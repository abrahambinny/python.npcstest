

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

API_URL = "https://10.1.3.95:8000/spservice/service?wsdl"
USERNAME = "soap_csys_infs"
PASSWORD = "76Hu25ZPNJzJ2k2N"

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

    return infs_resp

def infs_handle_np_request_cancel(csys_resp):

    client = get_api()
    infs_resp = client.service.HandleNpRequestCancel(
        ServiceType = csys_resp['ServiceType'],
        MessageCode = csys_resp['MessageCode'],
        Number = csys_resp['Number'],
        PortID = csys_resp['PortID'],
        SubmissionID = csys_resp['SubmissionID'],
        DonorID = csys_resp['DonorID'],
        RecipientID = csys_resp['RecipientID'],
        OriginationID = csys_resp['OriginationID'],
        DestinationID = csys_resp['DestinationID'],
    )

    print(infs_resp)
    return infs_resp


if __name__ == "__main__":

    csys_resp = {
        "ServiceType" : "F",
        "MessageCode" : "MessageAck",
        "Number" : "16511860",
        "PortID" : "INFX-INFS-20200716-00014",
        "SubmissionID" : "INFX-2020-07060060",
        "DonorID" : "INFS",
        "RecipientID" : "INFX",
        "OriginationID" : "CSYS",
        "DestinationID" : "INFX"
    }


    # infs_handle_np_request(client, csys_resp)
    infs_handle_np_request_cancel(csys_resp)
