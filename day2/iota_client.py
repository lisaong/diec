#
# IOTA client
# Author: Lisa Ong, NUS/ISS
#
# References:
# https://github.com/Hribek25/IOTA101
# https://medium.com/coinmonks/integrating-physical-devices-with-iota-83f4e00cc5bb

import sys
import iota
from iota.crypto.addresses import AddressGenerator
from iota.crypto.types import Seed
from pprint import pprint
import argparse
import time
import os

# https://docs.iota.org/docs/getting-started/0.1/references/iota-networks#devnet
node_config = {
    # https://github.com/iota-community/one-command-tangle
    # Then set the IOTA_TANGLE_URL environment variable
    'url': os.environ['IOTA_TANGLE_URL'],
    'min_weight_magnitude': 9
}

# security level for private key signature lengths
# https://docs.iota.org/docs/dev-essentials/0.1/references/security-levels
security_level = 2

def as_bytes(string):
    return bytes(string, 'ASCII')

def generate_addresses(count=1, seed=None):
    """Generates a number of IOTA addresses (given by count and optional seed)
    Returns: (address, seed)
    """
    if seed is None:
        seed = Seed.random()

    generator = AddressGenerator(seed=seed, security_level=security_level)
    return (generator.get_addresses(0, count), seed) # index, count

def get_balance(address_str):
    """Gets the balance of a given IOTA address
    If need to add tokens: https://faucet.devnet.iota.org/
    """
    address = iota.Address(as_bytes(address_str))
    api = iota.Iota(node_config['url'])
    return api.get_balances(addresses=[address], threshold=100)

def do_transaction(sender_seed_str, recipient_str, amount, message=None):
    """Performs an IOTA transaction with an optional message"""

    # address is a string 'ABCD...', convert to byte string b'ABCD...'
    recipient_address = iota.Address(as_bytes(recipient_str))

    # Once an address has been used to send tokens, it becomes useless
    # (a security hazard to reuse, because private key is compromised).
    # So we need to get a new address to hold the remaining tokens (if any).
    # The address must be retrieved using the sender's seed.
    #
    # This is also why we don't use sender address, but rather the sender seed
    change_address, _ = generate_addresses(1, sender_seed_str)

    print('Sending iotas ...')
    print('\tSender seed:', sender_seed_str)
    print('\tRecipient address:', recipient_str)
    print('\tAmount (iotas):', amount)
    print('\tChange address:', change_address[0])

    if message:
         # message needs to be encoded as tryte
         message = iota.TryteString.from_unicode(message)

    api = iota.Iota(node_config['url'], seed=sender_seed_str)
    output_tx = iota.ProposedTransaction(address=recipient_address,
             message=message,
             tag=iota.Tag(b'DIECWORKSHOPTWO'), # A-Z, 9
             value=amount)

    sent_bundle = api.send_transfer(depth=3,
             transfers=[output_tx],
             inputs=None, # using seed because address can change
             change_address=change_address[0], # where unspent tokens go
             min_weight_magnitude=node_config['min_weight_magnitude'],
             security_level=security_level)

    print("Done! Bundle hash: %s" % (sent_bundle['bundle'].hash))
    for tx in sent_bundle['bundle']:
        print("\n")
        pprint(vars(tx))
    return sent_bundle['bundle'].hash

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='IOTA client script for workshop')
    parser.add_argument('--gen_address', action='store_true', help='generates an IOTA address')
    parser.add_argument('--balance', metavar='ADDRESS', type=str, help='checks balance for a given IOTA address')

    # arguments for transactions
    tx_args = parser.add_argument_group('transaction arguments')
    tx_args.add_argument('--sender_seed', metavar='SEED', type=str, help='source seed for transaction')
    tx_args.add_argument('--to_address', metavar='ADDRESS', type=str, help='destination address for transaction')
    tx_args.add_argument('--amount', metavar='AMOUNT', type=int, help='amount of tokens to send')
    tx_args.add_argument('--message', type=str, help='optional transaction message')

    args = parser.parse_args()

    start = time.time()

    if args.gen_address:
        (address, seed) = generate_addresses()
        pprint(address)
        print(seed)
    elif args.balance:
        balance = get_balance(args.balance)
        pprint(balance)
    elif args.sender_seed and args.to_address and args.amount is not None:
        do_transaction(args.sender_seed, args.to_address, args.amount, args.message)
    else:
        parser.print_help()

    end = time.time()
    print('Elapsed Time:', end - start, 's')
