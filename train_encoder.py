import wikipedia, encoder
from pprint import pprint

def train():
	encodings = {}
	unicodes = str([chr(i) for i in range(0x077F)])
	(_,encodings) = encoder.unicode_encoder_simple(unicodes,encodings,0x077F)
	return encodings

if __name__ == '__main__':
	open('encodings.json','w').write(str(train()))
