from ADP_Request import APIRequest
from FileOpener import TextFileReader
from Dates import Dates
from Employees import Employees


def main():
    # Create employees object
    employees_object = Employees()
    # Call method to generate time cards

    # Single time card
    time_cards = employees_object.get_time_cards_current_week()
    print(len(time_cards))

    for time_card in time_cards:
        for person in time_card['teamTimeCards']:
            print(person['personLegalName']['formattedName'])

    # Multiple time cards
    # time_cards_list = employees_object.get_time_cards_from_date_range("2021-12-22", "2021-12-01")
    # for time_cards in time_cards_list:
    #     for time_card in time_cards:
    #         for person in time_card['teamTimeCards']:
    #             print(person['personLegalName']['formattedName'])



if __name__ == "__main__":
    main()
