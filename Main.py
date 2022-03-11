import time
from datetime import date, timedelta, datetime

import schedule

from Response_Filtering import ResponseFilter
from decimal import Decimal

from ADP_Request import APIRequest
from FileOpener import TextFileReader
from Dates import Dates
from Employees import Employees
from Response_Filtering import ResponseFilter
from Timecard import Timecard, Timecardv2, TimeEntry


# Gets single time card and adds the multiple responses to a list
def single_week_time_cards(date_within_pay_period: date):
    given_date = date_within_pay_period
    # employees_object = Employees()
    time_cards = Employees().get_time_cards_from_single_date(given_date)
    for time_card in time_cards:
        for person in time_card['teamTimeCards']:
            print(person['personLegalName']['formattedName'])
            print(person['timeCards'][0]['timePeriod']['startDate'])
    return time_cards


# Generates a list of time cards
def multiple_week_time_cards(date_within_first_pay_period: date, date_within_last_pay_period: date):
    # employees_object = Employees()
    time_cards_list = Employees().get_time_cards_from_date_range(date_within_first_pay_period,
                                                                      date_within_last_pay_period)
    for time_cards in time_cards_list:
        for time_card in time_cards:
            for person in time_card['teamTimeCards']:
                print(person['personLegalName']['formattedName'])
                print(person)
                # print(person['timeCards'][0]['timePeriod']['startDate'])
    return time_cards_list


def file_writer(file_name: str, time_card_object):
    try:
        file = open(fr"{file_name}.csv", "w")
        file.write(Timecard.csvTitles())
        for card in time_card_object:
            file.write(card.CsvStr())
        file.close()
    except:
        print("Error writing file SingleDay")


def main():
    # These two variables can be changed
    # This is where the files will be saved
    home_folder_path = "P:\\test\\"
    # This is the date used to generate the time card
    # Can be changed to date_obj = Dates("YYYY-MM-DD")
    # date_obj = Dates("2022-02-25")
    date_obj = Dates(date.today())

    # Generate Dates
    date_today = date_obj.return_given_date()
    date_yesterday = date_obj.get_date_yesterday()
    current_monday = date_obj.get_date_monday()
    previous_monday = date_obj.get_date_previous_monday()
    monday_before_previous = Dates(previous_monday).get_date_previous_monday()
    # print(date_today, date_yesterday, current_monday, previous_monday, monday_before_previous)

    # Get single day time_card
    this_week_time_cards_object = single_week_time_cards(date_yesterday)
    yesterdays_time_cards_filtered = ResponseFilter.timeCardHell(this_week_time_cards_object, str(date_yesterday))
    file_writer(f"{home_folder_path}Time_card_{str(date_yesterday)}", yesterdays_time_cards_filtered)

    # # Last week time cards

    # if date.weekday(date_today) == 4:
    #     last_week_time_cards_object = single_week_time_cards(previous_monday)
    #     last_week_time_cards_filtered = ResponseFilter.timeCardHell(last_week_time_cards_object)
    #     file_writer(f"{home_folder_path}Weekly_time_cards_starting_{str(previous_monday)}", last_week_time_cards_filtered)

    # Things that need to be done
    # Add to database if needed

if __name__ == "__main__":
    main()
