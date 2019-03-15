import argparse
import datetime
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

    except ApiException as e:
        print(f'Exception when calling API: {e}')

def get_account_id(name):
    scope_id = kapua_config.get_scope_id()
    try:
        api_client = kapua_config.get_api_client()
        api_instance = swagger_client.AccountsApi(api_client)
        api_response = api_instance.account_simple_query(scope_id, name=name, limit=1)

        if len(api_response.items) > 0:
            account_id = api_response.items[0].id
            print(f'Found account id: {account_id} for {name}')
            return account_id
        else:
            raise NameError(f'No account named {name} found')

    except ApiException as e:
        print(f'Exception when calling API: {e}')

def delete_account(name):
    scope_id = kapua_config.get_scope_id()
    try:
        api_client = kapua_config.get_api_client()
        api_instance = swagger_client.AccountsApi(api_client)

        account_id = get_account_id(name)
        api_instance.account_delete(scope_id, account_id)
        print(f'Deleted account id: {account_id}')

    except ApiException as e:
        print(f'Exception when calling API: {e}')

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
        print(f'Exception when calling API: {e}')

def get_user_id(account_id, name):
    try:
        api_client = kapua_config.get_api_client()
        api_instance = swagger_client.UsersApi(api_client)

        api_response = api_instance.user_simple_query(account_id, name=name, limit=1)

        if len(api_response.items) > 0:
            user_id = api_response.items[0].id
            print(f'Found user id: {user_id} for {name}')
            return user_id
        else:
            raise NameError(f'No user named {name} found')

    except ApiException as e:
        print(f'Exception when calling API: {e}')

def delete_user(account_id, name):
    try:
        user_id = get_user_id(account_id, name)

        api_client = kapua_config.get_api_client()
        api_instance.user_delete(account_id, user_id)
        print(f'Deleted user id: {user_id}')

    except ApiException as e:
        print(f'Exception when calling API: {e}')

def grant_permissions(account_id, user_id):
    try:
        api_client = kapua_config.get_api_client()
        api_instance = swagger_client.AccessInfoApi(api_client)

        # create access info
        body = swagger_client.AccessInfoCreator(user_id=user_id)
        api_response = api_instance.access_info_create(account_id, body)
        pprint(api_response)

        # add access permission
        access_info_id = api_response.id
        permission = swagger_client.Permission(target_scope_id=account_id)
        body = swagger_client.AccessPermissionCreator(permission=permission)
        api_response = api_instance.access_permission_create(account_id, access_info_id, body)
        pprint(api_response)

    except ApiException as e:
        print(f'Exception when calling API: {e}')    

def list_permissions(account_id, user_id):
    try:
        api_client = kapua_config.get_api_client()
        api_instance = swagger_client.AccessInfoApi(api_client)

        body = swagger_client.AccessInfoQuery()
        api_response = api_instance.access_info_query(account_id, body)
        print('AccessInfo:')
        pprint(api_response)
        access_info_id = api_response.items[0].id

        body = swagger_client.AccessPermissionQuery()
        api_response = api_instance.access_permission_query(account_id, access_info_id, body)
        print('Permissions:')
        pprint(api_response)

    except ApiException as e:
        print(f'Exception when calling API: {e}')    

def add_credentials(account_id, user_id, password):
    try:
        api_client = kapua_config.get_api_client()
        api_instance = swagger_client.CredentialsApi(api_client)

        expiration_date = datetime.date.today() + datetime.timedelta(days=365)

        # API key is generated by the server
        body = swagger_client.CredentialCreator(user_id=user_id,
            credential_type='API_KEY', credential_status='ENABLED',
            expiration_date=expiration_date)
        api_response = api_instance.credential_create(account_id, body)

        body = swagger_client.CredentialCreator(user_id=user_id,
            credential_type='PASSWORD', credential_status='ENABLED',
            credential_key=password,
            expiration_date=expiration_date)
        api_response = api_instance.credential_create(account_id, body)

    except ApiException as e:
        print(f'Exception when calling API: {e}')

def list_credentials(account_id, user_id):
    try:
        api_client = kapua_config.get_api_client()
        api_instance = swagger_client.CredentialsApi(api_client)

        api_response = api_instance.credential_simple_query(account_id, user_id=user_id, limit=50)
        pprint(api_response)

    except ApiException as e:
        print(f'Exception when calling API: {e}')

def get_api_key(account_id, user_id):
    try:
        api_client = kapua_config.get_api_client()
        api_instance = swagger_client.CredentialsApi(api_client)

        api_response = api_instance.credential_simple_query(account_id, user_id=user_id, limit=50)
        for i in api_response.items:
            if i.credential_type == 'API_KEY':
                return i.credential_key

        raise KeyError(f'No API key found for user {user_id}')

    except ApiException as e:
        print(f'Exception when calling API: {e}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Automates creation of Kapua accounts and users')
    parser.add_argument('command', type=str, choices=['add_acc', 'add_user', 'delete_user', 'delete_all'])

    args = parser.parse_args()

    # test values
    account = {
        'name': 'diec1',
        'email':'diec1@iss.edu',
        'org':'iss'
    }
    user = {
        'name': 'user1',
        'password': 'Kapu@12345678' # min 12 char, with special characters, upper
                                    # and lowercase, with numbers
    }

    if args.command == 'add_acc':
        create_account(name=account['name'], organization=account['org'], email=account['email'])
    else:
        account['id'] = get_account_id(name=account['name'])

        if args.command == 'add_user':
            user_id = create_user(account_id=account['id'], name=user)
            grant_permissions(account_id=account['id'], user_id=user_id)
            add_credentials(account_id=account['id'], user_id=user_id, password=user['password'])
            list_credentials(account_id=account['id'], user_id=user_id)

        elif args.command == 'delete_user':
            delete_user(account_id=account['id'], name=user['name'])

        elif args.command == 'delete_all':
            delete_user(account_id=account['id'], name=user['name'])
            delete_account(name=account['name'])
