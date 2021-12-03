from datetime import date, datetime, timedelta


# Class used to find first day of the week (date) when given a date within that specific pay period
class Dates:
    date_str: datetime
    first_date: datetime
    second_date: datetime

    def __init__(self, optional_first_date=date.today(), optional_second_date=date.today()):
        self.given_date = optional_first_date
        self.second_given_date = optional_second_date
        self.given_date = self.__check_type__(self.given_date)
        self.second_given_date = self.__check_type__(self.second_given_date)

    def __check_type__(self, date_as_str):
        self.date_str = date_as_str
        if type(self.date_str) is str:
            self.date_str = datetime.strptime(self.date_str, '%Y-%m-%d')
            self.date_obj = self.date_str.date()
        else: ## type(self.date_str) is datetime:
            self.date_str = datetime.strftime(self.date_str, '%Y-%m-%d')
            self.date_str = datetime.strptime(self.date_str, '%Y-%m-%d')
            self.date_obj = self.date_str.date()
        return self.date_obj

    def __get_monday__(self, random_date):
        self.random_date = random_date
        self.monday = self.random_date - timedelta(days=self.random_date.weekday())
        # self.monday = self.monday.strftime('%Y-%m-%d')
        return self.monday

    def __get_sunday__(self, random_date):
        self.random_date = random_date
        self.monday = self.__get_monday__(self.random_date)
        self.sunday = self.monday + timedelta(days=6)
        # self.sunday = self.monday.strftime('%Y-%m-%d')
        return self.sunday

    def get_date_monday(self):
        self.monday = self.__get_monday__(self.given_date)
        return self.monday

    def get_date_sunday(self):
        self.sunday = self.__get_sunday__(self.given_date)
        return self.sunday

    def get_list_of_mondays(self):
        self.monday_list = []
        self.first_monday = self.__get_monday__(self.given_date)
        self.last_monday = self.__get_monday__(self.second_given_date)
        self.current_monday = self.first_monday
        self.monday_list.append(self.first_monday)
        while self.current_monday != self.last_monday:
            self.current_monday = self.current_monday + timedelta(days=7)
            self.monday_list.append(self.current_monday)

            # self.current_monday = self.current_monday + timedelta(days=7)
        return self.monday_list


