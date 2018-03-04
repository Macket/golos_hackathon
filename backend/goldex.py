from nltk.stem import PorterStemmer


def index(query, objs, key):
    pst = PorterStemmer()
    query_tokens = list(map(lambda x: pst.stem(x.lower()), query.split()))
    result = []
    for obj in objs:
        stem_obj = pst.stem(key(obj).lower())
        if check_query_tokens_in_object(query_tokens, stem_obj):
            result.append(obj)

    return result


def check_query_tokens_in_object(query_tokens, stem_obj):
    for token in query_tokens:
        if token in stem_obj:
            return True

        if stem_obj in token:
            return True


if __name__ == '__main__':
    objs = [
        {'comment': {'name': 'Blockchainable', 'foo': 'bar_one'}, 'garb': 'one'},
        {'comment': {'name': 'Bitcoinainable', 'foo': 'bar_two'}, 'garb': 'two'},
        {'comment': {'name': 'unblockchain',   'foo': 'bar_three'}, 'garb': 'three'},
        {'comment': {'name': 'just blockchain', 'foo': 'bar_four'}, 'garb': 'four'},
        {'comment': {'name': 'blockchain', 'foo': 'bar_five'}, 'garb': 'five'},
    ]
    res = index('', objs, key=lambda x: x['comment']['name'])
    print(res)