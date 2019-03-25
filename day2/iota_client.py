# References:
# https://github.com/Hribek25/IOTA101

import iota
from iota.crypto.addresses import AddressGenerator
from iota.crypto.types import Seed
from pprint import pprint
import argparse
import time

# https://docs.iota.org/docs/getting-started/0.1/references/iota-networks#devnet
node_config = {
    'url': 'https://nodes.devnet.iota.org:443',
    'min_weight_magnitude': 9
}

security_level = 2

def generate_addresses(count):
    """Generates a number of IOTA addresses (given by count)"""
    seed = Seed.random()

    generator = AddressGenerator(seed=seed, security_level=security_level)
    return generator.get_addresses(0, count) # index, count

def get_balance(address):
    """Gets the balance of a given IOTA address"""
    api = iota.Iota(node_config['url'])

    # address is a string 'ABCD...', convert to byte string b'ABCD...'
    addresses = [iota.Address(bytes(address, 'ASCII'))]
    return api.get_balances(addresses)

def create_data_transaction(address, msg):
    """Creates a meta (data-only) IOTA transaction to an IOTA address
    """
    # https://iota.stackexchange.com/questions/328/what-are-trytes-and-trits
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
    parser.add_argument('--gen_address', type=int, help='generates the given number of IOTA addresses')
    parser.add_argument('--balance', type=str, help='checks balance for a given IOTA address')

    args = parser.parse_args()

    start = time.time()

    if args.gen_address is not None and args.gen_address > 0:
        addresses = generate_addresses(args.gen_address)
        pprint(addresses)
    elif args.balance is not None:
        balance = get_balance(args.balance)
        pprint(balance)
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
