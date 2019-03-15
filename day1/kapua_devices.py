import argparse
from pprint import pprint

 # Generated python client
import swagger_client
from swagger_client.rest import ApiException

import kapua_config
import kapua_accounts

def add_devices(account_name, user_name, device_names):
    print(device_names)
    pass

if __name__ == '__main__':

    # test values
    account_name = 'diec1'
    user_name = 'user1'

    parser = argparse.ArgumentParser(description='Automates creation of Kapua devices')
    parser.add_argument('--add', nargs='+', type=str, help='Adds one or more devices with the given names')
    parser.add_argument('--list', type=str, help='Lists all devices')
    parser.add_argument('--delete', nargs='+', type=str, help='Removes one or more devices with the given names')

    args = parser.parse_args()
    if args.add:
        add_devices(account_name, user_name, args.add)
    elif args.list:
        pass
    elif args.delete:
        pass


