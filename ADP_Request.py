import requests
import json
from datetime import date
from datetime import timedelta


# Class used to get bearer token and certain APIs
class APIRequest:
    def __init__(self, cert, associate_OID):
        self.files = {}
        self.payload = {}
        self.today = date.today()
        self.time_cards_list = []
        self.API_url_list = []
        self.certificate = cert
        self.associate_id = associate_OID


    # This method gets the token and returns it when called
    def get_token(self, authorization_token):
        # URL used to get the bearer token
        self.url = "https://accounts.adp.com/auth/oauth/v2/token?grant_type=client_credentials"
        self.auth_token = authorization_token
        self.headers = {
            'Authorization': 'Basic {0}'.format(self.auth_token)
        }
        self.response = requests.request("POST", url=self.url, headers=self.headers, data=self.payload,
                                         files=self.files, cert=self.certificate)
        # Loads the response into text format
        self.response_text = json.loads(self.response.text)
        # Retrieves the token from the response and assigns it to a variable
        self.token = self.response_text['access_token']
        # Adds the word 'Bearer' to the token since ADP requires it to be like that
        self.bearer_token = "Bearer " + self.token
        # Returns the token when the method is called
        return self.bearer_token

    def get_headers(self, bearer_token):
        self.bearer_token = bearer_token
        self.headers = {
            'Authorization': self.bearer_token,
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'api.adp.com',
            'Connection': 'Keep-Alive',
            'User-Agent': 'Apache-HttpClient/4.5.2(Java/1.8.0_112)',
            'Accept': 'application/json',
            'Cookie': 'BIGipServerp_dc1_mobile_sor_integratedezlm=3938124043.15395.0000; BIGipServerp_dc2_mobile_apache_sor=3013608203.5377.0000; BIGipServerp_mkplproxy-dc1=1633878283.20480.0000; BIGipServerp_mkplproxy-dc2=670892811.20480.0000; BIGipServerp_dc1_mobile_apache_sor=153042955.5377.0000; Cookie_1=value'
        }
        return self.headers


    def get_number_of_employees(self, headers, reference_date):
        self.headers = headers
        self.reference_date = str(reference_date)
        self.url = "https://api.adp.com/time/v2/workers/{0}/team-time-cards?$expand=dayEntries&$top=50&$filter=timeCards/timePeriod/startDate eq '{1}'".format(self.associate_id, self.reference_date)
        self.response = requests.request("GET", url=self.url, headers=self.headers, data=self.payload,
                                         files=self.files, cert=self.certificate)
        # Loads the response into text format
        self.response_text = json.loads(self.response.text)
        # Retrieves the number of employees from the response and assigns it to a variable
        self.number_of_employees = self.response_text['meta']['totalNumber']
        # Meta data indicates the timecard is not completele yet
        # self.response_text['meta']['completeIndicator'] == False
        # Returns the number of employees when the method is called
        return self.number_of_employees

    #Needs work
    #Will genearate a list of AOIDs from active and inactive employees
    def get_list_of_AOIDs(self, number_of_employees):
        pass