import numpy as np


class Encoder():
    """
    Encoder
    -------
    An encoder is
    simply a function
    from a Representation
    (both dense and sparse)
    to an SDR.
    This class has two methods:
    __init__()      : Assign encode with a custom encoding function
    encode()        : Encode an incoming numpy array of bools
    """
    def __init__(self, encoding_function):
        self.encode = encoding_function

def unicode_encoder_simple  (
                            msg,
                            encodings = {},
                            size_encoding = 256
                            ):

    encoding = []
    for i in range(len(msg)):
        if msg[i] in encodings:
            encoding.append(encodings[str(msg[i])])
        else:
            msg_i_encoding = (np.random.randn(size_encoding) > 0).tolist()
            while str(msg_i_encoding) in encodings:
                msg_i_encoding = (np.random.randn(size_encoding) > 0).tolist()
            encodings[str(msg[i])] = msg_i_encoding
            encoding.append(msg_i_encoding)
    return (encoding,encodings)
