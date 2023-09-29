def key_params(**kwargs):
    dict_ = {}
    for key_, value_ in kwargs.items():
        if isinstance(value_, (list, dict, set, bytearray)):
            value_ = str(value_)
        dict_[value_] = key_
    return dict_

print(key_params(a=1, b='hello', c=[1, 2, 3], d={}))
