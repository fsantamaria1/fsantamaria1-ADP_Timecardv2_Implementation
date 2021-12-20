from ADP_Request import APIRequest
from FileOpener import TextFileReader
from Dates import Dates
from Employees_Info import Employees


def main():
    employees_object = Employees()
    print(employees_object.bearer_token)
    print(employees_object.get_current_number_of_employees())


if __name__ == "__main__":
    main()
