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
                #print(person['timeCards'][0]['timePeriod']['startDate'])
    return time_cards_list


def main():
    # Generate Dates
    today = date.today()
    yesterday = today - timedelta(days=1)
    current_monday = Dates(today).get_date_monday()
    previous_monday = Dates(today).get_date_previous_monday()
    monday_before_previous = Dates(previous_monday).get_date_previous_monday()
    print(current_monday, previous_monday, monday_before_previous)

    # Yesterday's date
    yesterday = Dates.get_date_yesterday_string()
    print(yesterday)

    # Generate time card objects

    # Next pay period (current week) time cards
    # Can use any date within the pay period
    specific_date_time_cards = ResponseFilter.timeCardHell(single_week_time_cards(date.today()),
                                                             Dates.get_date_yesterday_string())  # << PUT DATE HERE
    try:
        # C:\Users\ccoon\Videos
        file = open(r"C:\Users\ccoon\Videos\adptest\ADPTEST_SingleDay.csv", "w")
        file.write(Timecard.csvTitles())
        for card in specific_date_time_cards:
            file.write(card.CsvStr())
        file.close()
    except:
        print("Error writing file SingleDay")

    # # Current pay period (last week) time cards
    # current_pay_period_time_cards = ResponseFilter.timeCardHell(single_week_time_cards(previous_monday))
    # try:
    #     file = open(r"C:\Users\ccoon\Videos\adptest\ADPTEST_CurrentPayPeriod.csv", "w")
    #     file.write(Timecard.csvTitles())
    #     for card in current_pay_period_time_cards:
    #         file.write(card.CsvStr())
    #     file.close()
    # except:
    #     print("Error writing file Current_Pay_Period")
    #
    # # Last pay period
    # previousPayPJS = single_week_time_cards(monday_before_previous)
    # print(previousPayPJS)
    # previous_pay_period_time_cards = ResponseFilter.timeCardHell(previousPayPJS)
    # try:
    #     file = open(r"C:\Users\ccoon\Videos\adptest\ADPTEST_PreviousPayPeriod.csv", "w")
    #     file.write(Timecard.csvTitles())
    #     for card in previous_pay_period_time_cards:
    #         file.write(card.CsvStr())
    #     file.close()
    # except:
    #     print("Error writing file Last_Pay_Period")
    #
    # # Get all three pay periods
    # dateRangeJS = multiple_week_time_cards(monday_before_previous, current_monday)
    # date_range_time_cards = ResponseFilter.timeCardHell(dateRangeJS)
    # try:
    #     file = open(r"C:\Users\ccoon\Videos\adptest\ADPTEST_DateRange.csv", "w")
    #     file.write(Timecard.csvTitles())
    #     for card in date_range_time_cards:
    #         file.write(card.CsvStr())
    #     file.close()
    # except:
    #      print("Error writing file Date_Range")

    # Things that need to be done
    # Add to database if needed

if __name__ == "__main__":
    main()
