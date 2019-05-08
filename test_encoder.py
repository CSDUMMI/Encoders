from encoder import Encoder, unicode_encoder_simple
import numpy as np


def test_unicode_encoder_simple():
    encoder = Encoder(unicode_encoder_simple)
    unicode_str = open('Albert_Schweitzer.txt').read()
    size = 5000
    (unicode_str_encoding,encodings) = encoder.encode(unicode_str,{},size_encoding=size)

    assert len(unicode_str_encoding) == len(unicode_str)
