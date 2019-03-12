import time
from pprint import pprint

 # Generated python client
import swagger_client
from swagger_client.rest import ApiException

import kapua_config

def create_account():
    try:
        api_client = kapua_config.get_api_client()
        api_instance = swagger_client.AccountsApi(api_client)

        # AccountCreator | Provides the information for the new Account to be created
        body = swagger_client.AccountCreator(name='diec', organization_name='iss',
            organization_email='diec@iss.edu')

        # Create an Account
        api_response = api_instance.account_create(kapua_config.get_scope_id(), body)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling API: %s\n" % e)

def list_accounts():
    try:
        api_client = kapua_config.get_api_client()
        api_instance = swagger_client.AccountsApi(api_client)

        api_response = api_instance.account_simple_query(kapua_config.get_scope_id(), name='diec', limit=1)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling API: %s\n" % e)    

if __name__ == '__main__':
    #create_account()
    list_accounts()