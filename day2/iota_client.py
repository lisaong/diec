# References:
# https://github.com/Hribek25/IOTA101

import iota
from iota.crypto.addresses import AddressGenerator
from iota.crypto.types import Seed
from pprint import pprint
import argparse
import time
import zmq

# https://docs.iota.org/docs/getting-started/0.1/references/iota-networks#devnet
node_config = {
    'url': 'https://nodes.devnet.iota.org:443',
    'min_weight_magnitude': 9,
    'zmq': 'tcp://zmq.devnet.iota.org:5556'
}

security_level = 2

def generate_addresses(count, seed=None):
    """Generates a number of IOTA addresses (given by count and optional seed)
    Returns: (address, seed)
    """
    if seed is None:
        seed = Seed.random()

    generator = AddressGenerator(seed=seed, security_level=security_level)
    return (generator.get_addresses(0, count), seed) # index, count

def str_to_address(address_str):
    # address is a string 'ABCD...', convert to byte string b'ABCD...'
    return iota.Address(bytes(address_str, 'ASCII'))

def get_balance(seed_str):
    """Gets the balance of a given IOTA address
    If need to add tokens: https://faucet.devnet.iota.org/
    """
    seed = bytes(seed_str, 'ASCII')
    api = iota.Iota(node_config['url'], seed)
    return api.get_account_data(start=0, stop=None)

def monitor(address_str):
    """Monitors a given address for a confirmed transaction

    References:
    https://docs.iota.org/docs/iri/0.1/references/zmq-events
    https://www.digitalocean.com/community/tutorials/how-to-work-with-the-zeromq-messaging-library
    """
    context = zmq.Context()

    # get a socket for our context
    sock = context.socket(zmq.SUB)

    # subscribe to this IOTA address
    sock.setsockopt(zmq.SUBSCRIBE, bytes(address_str, 'ASCII'))

    # Or subscribe to everything
    #sock.setsockopt(zmq.SUBSCRIBE, bytes('sn', 'ASCII'))

    sock.connect(node_config['zmq'])

    try:
        print('Monitoring transactions for', address_str)
        while True:
            message = sock.recv()
            print(message)
    finally:
        print('Closing socket')
        sock.close()

def do_transaction(sender_seed, to, amount, message='TESTDIECTRANSACTION'):
    """Performs a transaction
    message must only contain A-Z, 9
    """
    to_address = str_to_address(to)

    # Once an address has been used to send tokens, it becomes useless
    # (a security hazard to reuse, because private key is compromised).
    # So we need to get a new address to hold the remaining tokens (if any).
    # The address must be retrieved using the sender's seed.
    #
    # This is also why we don't use sender address, but rather the sender seed
    change_address, _ = generate_addresses(1, sender_seed)

    print('Sending iotas ...')
    print('\tSender seed:', sender_seed)
    print('\tRecipient address:', to)
    print('\tAmount (iotas):', amount)
    print('\tChange address:', change_address[0])

    api = iota.Iota(node_config['url'], seed=sender_seed)
    output_tx = iota.ProposedTransaction(address=to_address,
             message=message,
             tag=iota.Tag(b'DIECWORKSHOPDAYTWO'), # A-Z or 9
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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='IOTA client script for workshop')
    parser.add_argument('--gen_address', metavar='COUNT', type=int, help='generates the given number of IOTA addresses')
    parser.add_argument('--balance', metavar='SEED', type=str, help='checks balance for a given IOTA sender seed')
    parser.add_argument('--monitor', metavar='ADDRESS', type=str, help='monitors transactions for a given IOTA address')

    # arguments for transactions
    tx_args = parser.add_argument_group('transaction arguments')
    tx_args.add_argument('--sender_seed', metavar='SEED', type=str, help='source seed for transaction')
    tx_args.add_argument('--to_address', metavar='ADDRESS', type=str, help='destination address for transaction')
    tx_args.add_argument('--amount', metavar='AMOUNT', type=int, help='amount of tokens to send')

    args = parser.parse_args()

    start = time.time()

    if args.gen_address is not None and args.gen_address > 0:
        (addresses, seed) = generate_addresses(args.gen_address)
        pprint(addresses)
        print(seed)
    elif args.balance:
        balance = get_balance(args.balance)
        pprint(balance)
    elif args.monitor is not None:
        monitor(args.monitor)
    elif args.sender_seed and args.to_address and args.amount is not None:
        do_transaction(args.sender_seed, args.to_address, args.amount)
    else:
        parser.print_help()

    end = time.time()
    print('Elapsed Time:', end - start, 's')
