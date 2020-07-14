

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

API_URL = "https://10.1.3.95:8005/spservice/service?wsdl"
USERNAME = "soap_csys_infx"
PASSWORD = "UCkW7QuxAonKwGdr"

def get_api():


    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context

    client = Client(API_URL, username=USERNAME, password=PASSWORD, headers = {'username': USERNAME, 'password': PASSWORD})
    client.set_options(location=API_URL, soapheaders=(USERNAME, PASSWORD))

    print(client)


if __name__ == "__main__":

    get_api()
