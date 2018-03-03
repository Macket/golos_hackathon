import ipfsapi


class IpfsManager:
    def __init__(self):
        self._api = ipfsapi.connect('127.0.0.1', 5001)

    def add_video(self, name):
        self._api.add(name)

    def get_video(self, multihash):
        self._api.get(multihash)
