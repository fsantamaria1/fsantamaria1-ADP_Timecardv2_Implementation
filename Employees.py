import requests
import json

import ADP_Request

from Dates import Dates
# from ADP_Request import *

class Employees(ADP_Request.APIRequest):
    def __init__(self):
        super().__init__()
        # self.api_object = ADP_Request.APIRequest()
        #
        # self.bearer_token = self.api_object.get_token()
        # # self.time_card_headers = self.api_object.get_time_card_api_headers(self.bearer_token)
        # self.time_card_headers = self.api_object.get_time_card_api_headers(self.bearer_token)
        self.date_monday = Dates().get_date_monday()
        self.bearer_token = self.get_token()
        self.time_card_headers = self.get_time_card_api_headers(self.bearer_token)

    def __get_time_card__(self, top, skip, pay_period_start_date):
        self.date = pay_period_start_date
        self.top = 50
        self.skip = 0
        self.continue_request = True
        self.time_cards = []
        ## Add code to pull time card json

    def get_current_number_of_employees(self):
        """Returns the current number of active employees in ADP"""
        # self.reference_date = str(self.today)
        self.top = 50
        self.skip = 0
        self.url = self.generate_url(self.top, self.skip, self.date_monday)
        # self.url = "https://api.adp.com/time/v2/workers/{0}/team-time-cards?$expand=dayEntries&$top=50&$filter=timeCards/timePeriod/startDate eq '{1}'".format(
        #     self.associate_id, self.reference_date)
        self.response = requests.request("GET", url=self.url, headers=self.time_card_headers, data=self.payload,
                                         files=self.files, cert=self.certificate)
        # Loads the response into text format
        self.response_text = json.loads(self.response.text)
        # Retrieves the number of employees from the response and assigns it to a variable
        self.number_of_timecards = self.response_text['meta']['totalNumber']
        # Meta data indicates the time card response is not completed yet
        # self.response_text['meta']['completeIndicator'] == False
        # Returns the number of employees when the method is called
        return self.number_of_timecards
    def get_time_cards_current_week(self):
        self.top = 50
        self.skip = 0
        self.continue_request = True
        self.time_cards = []
        while self.continue_request == True:
            self.url = self.generate_url(self.top, self.skip, self.date_monday)
            print(self.url)
            self.top += 50
            self.skip += 50
            self.response = requests.request("GET", url=self.url, headers=self.time_card_headers, data=self.payload,
                                             files=self.files, cert=self.certificate)
            # Loads the response into text format
            self.response_text = json.loads(self.response.text)
            # Appends response to the list
            self.time_cards.append(self.response_text) # Might try extending the list instead
            # self.time_cards2.extend(self.response_text['teamTimeCards'])
            # Retrieves the number of employees from the response and assigns it to a variable
            if self.response_text['meta']['completeIndicator'] == True:
                self.continue_request = False
        return self.time_cards

