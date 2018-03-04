from collections import namedtuple
import json

import steem
from steembase.account import PasswordKey

SEARCH_ENTRY_FIELDS = ['name', 'author', 'description']
SearchEntry = namedtuple('SearchEntry', SEARCH_ENTRY_FIELDS)


_CHAIN_MASTER = None


def get_chain_master():
    if not _CHAIN_MASTER:
        return ChainMaster()

    return _CHAIN_MASTER


class ChainMaster:

    chain_master_prefix = 'chain-master-'

    def __init__(self):
        self._steem = steem.Steem(['https://ws.testnet3.golos.io'])
        self._username = 'chainmaster'
        self._password = 'qwerty12345'
        if not self._steem.steemd.login(self._username, self._password):
            raise RuntimeError('ChainMaster login failed!')

        key = PasswordKey(self._username, self._password, 'posting')
        self._steem.commit.wallet.setKeys(str(key.get_private()))
        print(1)

    def get_videos_list(self, query):
        all_videos = self._steem.steemd.get_blog(self._username, 0, 100)
        result = []
        for video in all_videos:
            if query in json.loads(video['comment']['json_metadata'])['name']:
                result.append(self._extract_search_entry(video))

        return result

    def get_video_metadata(self, name):
        permlink = self._get_permlink_from_name(name)
        return json.loads(self._steem.steemd.get_content(self._username, permlink)['json_metadata'])

    def add_video(self, name, author, description, multihash):
        json_payload = {
            'name': name,
            'author': author,
            'description': description,
            'multihash': multihash,
        }

        self._steem.commit.post(
            title=name,
            body='This post shall not be displayed',
            author=self._username,
            permlink=self._get_permlink_from_name(name),
            default_parent_permlink='videos',
            json_metadata=json_payload
        )

    def _extract_search_entry(self, video):
        return {field: json.loads(video['comment']['json_metadata'])[field] for field in SEARCH_ENTRY_FIELDS}

    def _get_permlink_from_name(self, name):
        return self.chain_master_prefix + name

    def _get_name_from_permlink(self, permlink):
        return permlink[len(self.chain_master_prefix):]

    def __identity(self, x):
        return x
