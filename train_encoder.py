import wikipedia, encoder
from pprint import pprint

def train():
	encodings = {}
	unicodes = str([chr(i) for i in range(int(0x10FFFF / 1000))])
	(_,encodings) = encoder.unicode_encoder_simple(unicodes,encodings,0x10FFFF+0xFF)
	return encodings

if __name__ == '__main__':
	open('encodings.json','w').write(str(train()))
