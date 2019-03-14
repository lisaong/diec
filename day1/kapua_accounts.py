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
        print(f'Created account with id: {api_response.id}')
        return api_response.id

    except ApiException as e:
        print("Exception when calling API: %s\n" % e)

def get_account_id(name):
    scope_id = kapua_config.get_scope_id()
    try:
        api_client = kapua_config.get_api_client()
        api_instance = swagger_client.AccountsApi(api_client)

        api_response = api_instance.account_simple_query(scope_id, name=name, limit=1)
        pprint(api_response)

        if len(api_response.items) > 0:
            account_id = api_response.items[0].id
            print(f'Found account id: {account_id} for {name}')
            return account_id
        else:
            raise NameError(f'No account named {name} found')

    except ApiException as e:
        print("Exception when calling API: %s\n" % e)    

def delete_account(name):
    scope_id = kapua_config.get_scope_id()
    try:
        api_client = kapua_config.get_api_client()
        api_instance = swagger_client.AccountsApi(api_client)

        account_id = get_account_id(name)
        api_instance.account_delete(scope_id, account_id)

    except ApiException as e:
        print("Exception when calling API: %s\n" % e)

def create_user(account_id, name):
    try:
        api_client = kapua_config.get_api_client()
        api_instance = swagger_client.UsersApi(api_client)

        body = swagger_client.UserCreator(name=name)
        api_response = api_instance.user_create(account_id, body)
        pprint(api_response)

        print(f'Created user {name} for account {account_id} with id: {api_response.id}')
        return api_response.id

    except ApiException as e:
        print("Exception when calling API: %s\n" % e)

def delete_user(account_id, name):
    try:
        api_client = kapua_config.get_api_client()
        api_instance = swagger_client.UsersApi(api_client)

        api_response = api_instance.user_simple_query(account_id, name=name, limit=1)

        if len(api_response.items) > 0:
            user_id = api_response.items[0].id
            print(f'Found user id: {user_id}')
            api_instance.user_delete(account_id, user_id)
        else:
            print(f'No user named {name} found for account {account_id}')

    except ApiException as e:
        print("Exception when calling API: %s\n" % e)

def list_users(account_id=None):
    if not account_id:
        account_id = kapua_config.get_scope_id()

    try:
        api_client = kapua_config.get_api_client()
        api_instance = swagger_client.UsersApi(api_client)

        body = swagger_client.UserQuery()

        api_response = api_instance.user_query(account_id, body)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling API: %s\n" % e)

if __name__ == '__main__':
    #account_id = create_account(name='diec', organization='iss', email='diec@iss.edu')

    account_id = get_account_id(name='diec')
    #create_user(account_id=account_id, name='user1')
    #list_users(account_id=account_id)

    #delete_user(account_id=account_id, name='user1')
    #delete_account(name='diec')
