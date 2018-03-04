import steem
from steem.account import Account
from steembase.transactions import SignedTransaction
from steembase import bip38, base58
from steembase.account import PasswordKey


def main():
    pkey = PasswordKey('poster', 'qwerty12345', 'posting')
    passphrase = 'blabla'
    post_wif = '5KjSBXNv9igFyo761qiqdKgsYxKAi5PNiZ424mSbvAvFc4382y1'
    st = steem.Steem(['https://ws.testnet3.golos.io'])
    account = st.steemd.get_account('poster')
    config = st.steemd.get_config()
    is_login = st.steemd.login('poster', 'qwerty12345')
    if not is_login:
        raise ValueError('Unable to login')

    st.commit.wallet.setKeys(post_wif)
    poster = st.steemd.get_account('poster')
    st.commit.post('Privet5', 'Blablabla5', 'poster', permlink='verify', default_parent_permlink='video')

    print(1)


if __name__ == '__main__':
    main()
