from encoder import Encoder, unicode_encoder_simple
import numpy as np


def test_unicode_encoder_simple():
    unicode_str = open('Albert_Schweitzer.txt').read()
    size = 5000
    (unicode_str_encoding,encodings) = unicode_encoder_simple(unicode_str,{},size_encoding=size)

    assert unicode_str_encoding.shape == (len(unicode_str)*size,)
