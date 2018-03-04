import os

import ipfsapi

IPFS_API = None


def get_ipfsapi():
    if not IPFS_API:
        return IpfsApi()

    return IPFS_API


class IpfsApi:
    def __init__(self):
        self._api = ipfsapi.connect('127.0.0.1', 5001)

    def add_video(self, name):
        self._api.add(name)

    def get_video(self, multihash, path):
        self._api.get(multihash)
        os.rename('{}'.format(multihash), path)
