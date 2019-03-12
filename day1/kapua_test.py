import time
from pprint import pprint

 # Generated python client
import swagger_client
from swagger_client.rest import ApiException

import kapua_config

try:
    # Authenticate an API user
    api_client = kapua_config.get_api_client()
    pprint(api_client.configuration.api_key)

    users_api = swagger_client.UsersApi(api_client)
    scope_id = kapua_config.SCOPE_ID # str | The ScopeId in which to count results
    body = swagger_client.UserQuery() # UserQuery | The UserQuery to use to filter count results

    # Count the number of users
    users_response = users_api.user_count(scope_id, body)
    pprint(users_response)

except ApiException as e:
    print("Exception when calling API: %s\n" % e)
