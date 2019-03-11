import swagger_client # Generated python client
from swagger_client.rest import ApiException

from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi()

# ApiKeyCredentials | The API KEY authentication credential of a user.
body = swagger_client.ApiKeyCredentials(api_key='12345678kapua-password') # ApiKeyCredentials | The API KEY authentication credential of a user.

try:
    # Authenticate an API user
    api_response = api_instance.authentication_api_key(body)
    pprint(api_response)

    # Get the token id for future requests
    token_id = api_response.token_id

    # Get 

except ApiException as e:
    print("Exception when calling AuthenticationApi->authentication_api_key: %s\n" % e)
