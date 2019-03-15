import argparse
from pprint import pprint

 # Generated python client
import swagger_client
from swagger_client.rest import ApiException

import kapua_config
import kapua_accounts

def add_devices(account_id, user_id, device_names):
    print(device_names)

    api_client = kapua_config.get_api_client(api_key='QJ1ixt7HF8yf10dc5M3F6bRw6kvjFNahT7pyr5fA')
    pprint(api_client)

if __name__ == '__main__':

    # test values
    account_name = 'diec1'
    user_name = 'user1'

    parser = argparse.ArgumentParser(description='Automates creation of Kapua devices')
    parser.add_argument('--add', nargs='+', type=str, help='Adds one or more devices with the given names')
    parser.add_argument('--list', type=str, help='Lists all devices')
    parser.add_argument('--delete', nargs='+', type=str, help='Removes one or more devices with the given names')

    args = parser.parse_args()

    account_id = kapua_accounts.get_account_id(name=account_name)
    user_id = kapua_accounts.get_user_id(account_id=account_id, name=user_name)

    if args.add:
        add_devices(account_id, user_id, args.add)
    elif args.list:
        pass
    elif args.delete:
        pass


