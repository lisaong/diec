import time
from pprint import pprint

 # Generated python client
import swagger_client
from swagger_client.rest import ApiException

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi()

# ApiKeyCredentials | The API KEY authentication credential of a user.
body = swagger_client.ApiKeyCredentials(api_key='12345678kapua-password') # ApiKeyCredentials | The API KEY authentication credential of a user.

try:
    # Authenticate an API user
    api_response = api_instance.authentication_api_key(body)
    pprint(api_response)

    # Set the token id as the Auth token
    configuration = swagger_client.Configuration()
    configuration.api_key['Authorization'] = api_response.token_id

    users_api = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
    scope_id = '_' # str | The ScopeId in which to count results
    body = swagger_client.UserQuery() # UserQuery | The UserQuery to use to filter count results

    # Count the number of users
    users_response = users_api.user_count(scope_id, body)
    pprint(users_response)

except ApiException as e:
    print("Exception when calling API: %s\n" % e)
