from datetime import date, datetime, timedelta

#Class used to find first day of the week (date) when given a date whithin that specific pay period
class Dates:
    def __init__(self, specific_date=str(date.today())):
        self.given_date = specific_date
    def get_first_day_of_week(self):
        #Create date object from given date
        self.date_obj = datetime.strptime(self.given_date, '%Y-%m-%d')
        # Find start of week based on given date
        self.start_of_week = self.date_obj - timedelta(days=self.date_obj.weekday())
        #Convert date to YYYY-MM-DD format
        self.start_of_week = datetime.date(self.start_of_week)
        return self.start_of_week

    def get_last_day_of_week(self):
        # Create date object from given date
        self.date_obj = datetime.strptime(self.given_date, '%Y-%m-%d')
        # Find start of week based on given date
        self.start_of_week = self.date_obj - timedelta(days=self.date_obj.weekday())
        # Find end of week based on given date
        self.end_of_week = self.start_of_week + timedelta(days=6)
        # Convert date to YYYY-MM-DD format
        self.end_of_week = datetime.date(self.end_of_week)
        return self.end_of_week

