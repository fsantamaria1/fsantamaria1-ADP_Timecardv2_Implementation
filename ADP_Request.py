import requests
import json
from datetime import date
from datetime import timedelta


# Class used to get bearer token and certain APIs
class APIRequest:
    def __init__(self, cert):
        self.certificate = cert
        # URL used to get the bearer token
        self.url = "https://accounts.adp.com/auth/oauth/v2/token?grant_type=client_credentials"

    # This method gets the token and returns it when called
    def get_token(self, authorization_token):
        self.payload = {}
        self.files = {}
        self.auth_token = authorization_token
        self.headers = {
            'Authorization': 'Basic {0}'.format(self.auth_token)
        }
        self.response = requests.request("POST", url=self.url, headers=self.headers, data=self.payload,
                                         files=self.files, cert=self.certificate)
        # Loads the response into text format
        self.bearerTokenResponse = json.loads(self.response.text)
        # Retrieves the token from the response and assigns it to a variable
        self.token = self.bearerTokenResponse['access_token']
        # Adds the word 'Bearer' to the token since ADP requires it to be like that
        self.bearerToken = "Bearer " + self.token
        # Returns the token when the method is called
        return (self.bearerToken)



