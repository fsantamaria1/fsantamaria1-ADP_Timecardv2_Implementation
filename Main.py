from datetime import date, timedelta
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
    employees_object = Employees()
    time_cards_list = employees_object.get_time_cards_from_date_range(date_within_first_pay_period,
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
        # C:\Users\ccoon\Videos
        # file = open(r"C:\Users\ccoon\Videos\adptest\ADPTEST_SingleDay.csv", "w")
        file = open(fr"P:\{file_name}.csv", "w")
        file.write(Timecard.csvTitles())
        for card in time_card_object:
            file.write(card.CsvStr())
        file.close()
    except:
        print("Error writing file SingleDay")


def main():
    # Generate Dates
    today = date.today()
    yesterday = today - timedelta(days=1)
    current_monday = Dates(today).get_date_monday()
    previous_monday = Dates(today).get_date_previous_monday()
    monday_before_previous = Dates(previous_monday).get_date_previous_monday()
    print(current_monday, previous_monday, monday_before_previous)

    # Dates as string
    yesterday_string = Dates.get_date_yesterday_string()
    today_string = Dates.get_date_today_string()

    # Can use any date within the pay period

    # Get single day time_card
    this_week_time_cards_object = single_week_time_cards(today_string)
    yesterdays_time_cards_filtered = ResponseFilter.timeCardHell(this_week_time_cards_object, yesterday_string)
    file_writer(f"Time_card_{yesterday_string}", yesterdays_time_cards_filtered)

    # Last week time cards
    last_week_time_cards_object = single_week_time_cards(str(previous_monday))
    last_week_time_cards_filtered = ResponseFilter.timeCardHell(last_week_time_cards_object)
    file_writer(f"Weekly_time_cards_{str(previous_monday)}", last_week_time_cards_filtered)

    # Things that need to be done
    # Add to database if needed


if __name__ == "__main__":
    main()
