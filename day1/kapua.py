# Generated python client
import time

# Generated python client
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi()

# ApiKeyCredentials | The API KEY authentication credential of a user.
body = swagger_client.ApiKeyCredentials(api_key='12345678kapua-password') # ApiKeyCredentials | The API KEY authentication credential of a user.

try:
    # Authenticate an user
    api_response = api_instance.authentication_api_key(body)
    print(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->authentication_api_key: %s\n" % e)
