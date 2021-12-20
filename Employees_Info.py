import requests
import json

import ADP_Request
# from ADP_Request import *

class Employees(ADP_Request.APIRequest):
    def __init__(self):
        super().__init__()
        # self.api_object = ADP_Request.APIRequest()
        #
        # self.bearer_token = self.api_object.get_token()
        # # self.time_card_headers = self.api_object.get_time_card_api_headers(self.bearer_token)
        # self.time_card_headers = self.api_object.get_time_card_api_headers(self.bearer_token)
        self.bearer_token = self.get_token()
        self.time_card_headers = self.get_time_card_api_headers(self.bearer_token)

    def get_current_number_of_employees(self):
        """Returns the current number of active employees in ADP"""
        self.reference_date = str(self.today)

        self.url = "https://api.adp.com/time/v2/workers/{0}/team-time-cards?$expand=dayEntries&$top=50&$filter=timeCards/timePeriod/startDate eq '{1}'".format(
            self.associate_id, self.reference_date)
        self.response = requests.request("GET", url=self.url, headers=self.time_card_headers, data=self.payload,
                                         files=self.files, cert=self.certificate)
        # Loads the response into text format
        self.response_text = json.loads(self.response.text)
        # Retrieves the number of employees from the response and assigns it to a variable
        self.number_of_timecards = self.response_text['meta']['totalNumber']
        # Meta data indicates the timecard is not completele yet
        # self.response_text['meta']['completeIndicator'] == False
        # Returns the number of employees when the method is called
        return self.number_of_timecards
