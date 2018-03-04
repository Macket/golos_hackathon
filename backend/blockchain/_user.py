from enum import Enum

import steem
from steembase.account import PasswordKey

from ipfs import get_ipfsapi


def login(username, password):
    st = steem.Steem(['https://ws.testnet3.golos.io'])
    if not st.steemd.login(username, password):
        return None

    private_key = PasswordKey(username, password, 'posting')
    st.commit.wallet.setKeys(private_key.get_private())
    return User(username, password, st)


class VoteType(Enum):
    UP_VOTE = -1,
    DOWN_VOTE = 1


class User:
    def __init__(self, username, password, steem):
        self._username = username
        self._passwd = password
        self._steem = steem
        self._ipfsapi = get_ipfsapi()

    @staticmethod
    def get_videos_list(query):
        pass

    @staticmethod
    def get_video(name, path):
        # TODO: get video hash from phantom user
        multihash = None
        get_ipfsapi().get_video(multihash, path)

    def add_video(self, name):
        pass

    def vote_video(self, name, type):
        pass
