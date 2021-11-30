from ADP_Request import APIRequest
from FileOpener import TextFileReader
from Dates import Dates


def main():
    # PEM file path
    cert_file_path = r"C:\ADP API\Certificates\berryit_auth.pem"
    # KEY file path
    key_file_path = r"C:\ADP API\Certificates\berryit_auth.key"
    # Both files combined
    cert = (cert_file_path, key_file_path)
    # Authorization token file path
    auth_token_path = r"Y:\05 Users\Cossell\ADP API\Certificates\auth_token_encrypted.txt"
    # Associate AOID file path
    aoid_path = r"Y:\05 Users\Cossell\ADP API\Certificates\AOID.txt"
    # Read and assign auth token to variable
    auth_token = TextFileReader(auth_token_path).read_first_line()
    # Get Associate OID
    associate_id = TextFileReader(aoid_path).read_first_line()
    # Create ADP API class object
    ADP_object = APIRequest(cert, associate_id)
    # Assign bearer token to variable
    bearer_token = ADP_object.get_token(auth_token)
    # Will need to figure out a better way to deal with the dates
    # Gets first date of a pay period based on a date
    first_date_within_pay_period = Dates("2021-10-01").get_first_day_of_week()
    # Gets last date of a pay period based on a date
    last_date_within_pay_period = Dates("2021-10-01").get_last_day_of_week()
    #Generate headers
    headers = ADP_object.get_headers(bearer_token)
    number_of_employees = ADP_object.get_number_of_employees(headers, first_date_within_pay_period)
    print("Number of Employees: ", number_of_employees)


if __name__ == "__main__":
    main()
