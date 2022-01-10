from datetime import date, timedelta

from ADP_Request import APIRequest
from FileOpener import TextFileReader
from Dates import Dates
from Employees import Employees
from Response_Filtering import ResponseFilter
from Timecard import Timecard


# Gets single time card and adds the multiple responses to a list
def single_week_time_cards(date_within_pay_period: date):
    employees_object = Employees()
    time_cards = employees_object.get_time_cards_from_single_date(date_within_pay_period)
    for time_card in time_cards:
        for person in time_card['teamTimeCards']:
            print(person['personLegalName']['formattedName'])
    return time_cards


# Generates a list of time cards
def multiple_week_time_cards(date_within_first_pay_period: date, date_within_last_pay_period: date):
    employees_object = Employees()
    time_cards_list = employees_object.get_time_cards_from_date_range(date_within_first_pay_period,
                                                                      date_within_last_pay_period)
    for time_cards in time_cards_list:
        for time_card in time_cards:
            for person in time_card['teamTimeCards']:
                print(person['personLegalName']['formattedName'])
    return time_cards_list


def main():
    # Generate Dates
    today = date.today()
    yesterday = today - timedelta(days=1)
    current_monday = Dates(today).get_date_monday()
    previous_monday = Dates(today).get_date_previous_monday()
    monday_before_previous = Dates(previous_monday).get_date_previous_monday()
    print(current_monday, previous_monday, monday_before_previous)

    # Generate time card objects

    # Next pay period (current week) time cards
    # Can use any date within the pay period
    next_pay_period_time_cards = single_week_time_cards(date.today())
    # Current pay period (last week) time cards
    current_pay_period_time_cards = single_week_time_cards(previous_monday)
    # Last pay period
    previous_pay_period_time_cards = single_week_time_cards(monday_before_previous)
    # Get all three pay periods
    date_range_time_cards = multiple_week_time_cards(monday_before_previous, current_monday)

    # Things that need to be done
    # Filter responses
    # Generate a CSV
    # Add to database if needed

    # TCards = ResponseFilter.createTimecard()


if __name__ == "__main__":
    main()
