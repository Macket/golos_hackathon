from collections import namedtuple
from enum import Enum

import steem
from steembase.account import PasswordKey
from steem.post import Post

from ..ipfs import get_ipfsapi
from ._chain_master import get_chain_master


def login(username, password):
    st = steem.Steem(['https://ws.testnet3.golos.io'])
    if not st.steemd.login(username, password):
        return None

    private_key = PasswordKey(username, password, 'posting')
    st.commit.wallet.setKeys(str(private_key.get_private()))
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
        self._cur_post = None

    @staticmethod
    def get_videos_list(query):
        return get_chain_master().get_videos_list(query)

    @staticmethod
    def get_video_unauthorized(name, path):
        video_metadata = get_chain_master().get_video_metadata(name)
        multihash = video_metadata['multihash']
        get_ipfsapi().get_video(multihash, path)
        return video_metadata

    def get_video(self, name, path):
        video_metadata = User.get_video_unauthorized(name, path)
        self._cur_post = Post({
            'author': video_metadata['author'],
            'permlink': video_metadata['name'],
        }, self._steem)
        return self._cur_post

    def add_video(self, name, path, description=None):
        description = description or 'No description'
        result = self._ipfsapi.add_video(path)
        get_chain_master().add_video(name, self._username, description, result['Hash'])
        self._steem.commit.post(
            title=name,
            body=description,
            author=self._username,
            permlink=name,
            default_parent_permlink='video'
        )

    def vote_video(self, type):
        if not self._cur_post:
            raise RuntimeError('There is no post to vote')

        if type == VoteType.UP_VOTE:
            return self._cur_post.upvote(self._username)

        return self._cur_post.downvote(self._username)
