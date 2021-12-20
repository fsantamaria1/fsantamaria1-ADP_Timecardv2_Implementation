from ADP_Request import APIRequest
from FileOpener import TextFileReader
from Dates import Dates
from Employees import Employees


def main():
    # Create employees object
    employees_object = Employees()
    # Call method to generate time cards
    time_cards = employees_object.get_time_cards_current_week()
    for time_card in time_cards:
        for person in time_card['teamTimeCards']:
            print(person['personLegalName']['formattedName'])

if __name__ == "__main__":
    main()
