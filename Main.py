from ADP_Request import APIRequest
from FileOpener import TextFileReader


def main():
    # PEM file path
    cert_file_path = r"C:\ADP API\Certificates\berryit_auth.pem"
    # KEY file path
    key_file_path = r"C:\ADP API\Certificates\berryit_auth.key"
    # Both files combined
    cert = (cert_file_path, key_file_path)
    # Authorization token file path
    auth_token_path = r"Y:\05 Users\Cossell\ADP API\Certificates\auth_token_encripted.txt"
    # Read and assign auth token to variable
    auth_token = TextFileReader(auth_token_path).read_first_line()
    # Assign bearer token to variable
    bearer_token = APIRequest(cert).get_token(auth_token)





if __name__ == "__main__":
    main()
