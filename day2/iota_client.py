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
    'zmq': 'tcp://zmq.testnet.iota.org:5556'
}

security_level = 2

def generate_addresses(count):
    """Generates a number of IOTA addresses (given by count)"""
    seed = Seed.random()

    generator = AddressGenerator(seed=seed, security_level=security_level)
    return generator.get_addresses(0, count) # index, count

def str_to_address(address_str):
    # address is a string 'ABCD...', convert to byte string b'ABCD...'
    return iota.Address(bytes(address, 'ASCII'))

def get_balance(address_str):
    """Gets the balance of a given IOTA address"""
    api = iota.Iota(node_config['url'])

    addresses = [str_to_address(address)]
    return api.get_balances(addresses)

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
    sock.setsockopt(zmq.SUBSCRIBE, str_to_address(address))
    sock.connect(node_config['zmq'])
    sock.RCVTIMEO = 3000 # timeout (milliseconds)

    try:
        while True:
            message = sock.recv()
            print(message)
    finally:
        sock.close()


def create_data_transaction(address, msg):
    """Creates a meta (data-only) IOTA transaction to an IOTA address
    """
    return iota.ProposedTransaction(address=address, message=iota.TryteString.from_unicode(msg),
             tag=iota.Tag(b'DIECPYOTAWORKSHOP'), value=0)

def create_bundle(transactions):
    """Creates an IOTA bundle from a list of transactions"""
    bundle = iota.ProposedBundle(transactions=transactions)
    bundle.finalize()
    return bundle

def perform_pow(bundle):
    """Performs a proof of work on a bundle"""
    api = iota.Iota(node_config['url'])

    # depth: how many milestones to go in the past
    # Higher value has better network, but requires more resources
    tips = api.get_transactions_to_approve(depth=2)
    att = api.attach_to_tangle(trunk_transaction=tips['trunkTransaction'], # first tip
              branch_transaction=tips['branchTransaction'], # second tip
              trytes=bundle.as_tryte_strings(),
              min_weight_magnitude=node_config['min_weight_magnitude'])

    res = api.broadcast_and_store(att['trytes'])
    return res, att

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='IOTA client script for workshop')
    parser.add_argument('--gen_address', metavar='COUNT', type=int, help='generates the given number of IOTA addresses')
    parser.add_argument('--balance', metavar='ADDRESS', type=str, help='checks balance for a given IOTA address')
    parser.add_argument('--monitor', metavar='ADDRESS', type=str, help='monitors transactions for a given IOTA address')

    args = parser.parse_args()

    start = time.time()

    if args.gen_address is not None and args.gen_address > 0:
        addresses = generate_addresses(args.gen_address)
        pprint(addresses)
    elif args.balance is not None:
        balance = get_balance(args.balance)
        pprint(balance)
    elif args.monitor is not None:
        monitor(args.monitor)
    else:
        parser.print_help()

    #tx = create_data_transaction(addresses[0], 'hello')
    #pprint(vars(tx))

    #pb = create_bundle([tx])
    #print('Bundle hash', pb.hash)

    #res, att = perform_pow(pb)

    # show what has been broadcasted - hash transaction + nonce (POW)
    #print("Final bundle including POW and branch/trunk transactions:")
    #for t in att['trytes']:
    #    pprint(vars(iota.Transaction.from_tryte_string(t)))
    #    print("")

    #print('Broadcast result:')
    #pprint(res)

    end = time.time()
    print('Elapsed Time:', end - start, 's')
