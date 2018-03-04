_CHAIN_MASTER = None


def get_chain_master():
    if not _CHAIN_MASTER:
        return ChainMaster()

    return _CHAIN_MASTER


class ChainMaster:
    def __init__(self):
        pass
