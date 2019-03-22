# References:
# https://github.com/Hribek25/IOTA101/blob/master/01_IOTA%20Essentials.ipynb

import iota
from iota.crypto.addresses import AddressGenerator
from iota.crypto.types import Seed
from pprint import pprint
import time

node_url = 'https://nodes.thetangle.org:443'
security_level = 2

def generate_seed():
    return Seed.random()

def generate_addresses(seed, count):
    generator = AddressGenerator(seed=seed, security_level=security_level)
    return generator.get_addresses(0, count) # index, count

def create_data_transaction(addresses):
    """Creates a meta (data-only) transaction to addresses
    """
    pass

if __name__ == "__main__":
    start = time.time()
    seed = generate_seed()
    print('Seed:', seed)
    addresses = generate_addresses(seed, 2)
    pprint(addresses)
    end = time.time()
    print('Elapsed Time:', end - start, 's')
