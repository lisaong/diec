#
# Common configuration and code for Kapua REST API client
# Author: Lisa Ong, NUS/ISS
#

# Generated python client
import swagger_client

def get_scope_id():
    SCOPE_ID = '_'
    return SCOPE_ID

def get_api_client(api_key=None):
    if not api_key:
        # kapua-sys's API key
        api_key = '12345678kapua-password'
    
    # create an instance of the API class
    api_instance = swagger_client.AuthenticationApi()

    # ApiKeyCredentials | The API KEY authentication credential of a user.
    body = swagger_client.ApiKeyCredentials(api_key=api_key)

    # Authenticate an API user
    api_response = api_instance.authentication_api_key(body)

    # Set the token id as the Auth token
    configuration = swagger_client.Configuration()
    configuration.api_key['Authorization'] = api_response.token_id
    return swagger_client.ApiClient(configuration)