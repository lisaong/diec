import time
from pprint import pprint

 # Generated python client
import swagger_client
from swagger_client.rest import ApiException

import kapua_config

def create_account(name, organization, email):
    scope_id = kapua_config.get_scope_id()
    try:
        api_client = kapua_config.get_api_client()
        api_instance = swagger_client.AccountsApi(api_client)

        # AccountCreator | Provides the information for the new Account to be created
        body = swagger_client.AccountCreator(name=name, organization_name=organization, organization_email=email)

        # Create an Account
        api_response = api_instance.account_create(scope_id, body)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling API: %s\n" % e)

def list_accounts():
    scope_id = kapua_config.get_scope_id()
    try:
        api_client = kapua_config.get_api_client()
        api_instance = swagger_client.AccountsApi(api_client)

        api_response = api_instance.account_simple_query(scope_id, limit=1)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling API: %s\n" % e)    

def create_user(name):
    scope_id = kapua_config.get_scope_id()
    try:
        api_client = kapua_config.get_api_client()
        api_instance = swagger_client.UsersApi(api_client)

        body = swagger_client.UserCreator(name=name)
        api_response = api_instance.user_create(scope_id, body)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling API: %s\n" % e)

def delete_user(name):
    scope_id = kapua_config.get_scope_id()

    try:
        api_client = kapua_config.get_api_client()
        api_instance = swagger_client.UsersApi(api_client)

        api_response = api_instance.user_simple_query(scope_id, name=name, limit=1)

        if len(api_response.items) > 0:
            user_id = api_response.items[0].id
            pprint(f'Found user id: {user_id}')
            api_instance.user_delete(scope_id, user_id)

    except ApiException as e:
        print("Exception when calling API: %s\n" % e)

def list_users(scope_id=None):
    if not scope_id:
        scope_id = kapua_config.get_scope_id()

    try:
        api_client = kapua_config.get_api_client()
        api_instance = swagger_client.UsersApi(api_client)

        body = swagger_client.UserQuery()

        api_response = api_instance.user_query(scope_id, body)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling API: %s\n" % e)

if __name__ == '__main__':
    #create_account(name='diec', organization='iss', email='diec@iss.edu')
    list_accounts()
    create_user(name='user1')
    list_users()
