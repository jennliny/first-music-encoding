import music21
from music21 import *

url = 'http://kern.ccarh.org/cgi-bin/ksdata?l=cc/bach/cello&file=bwv1007-01.krn&f=xml'
sAlt = converter.parse(url)
print(sAlt.measures(1, 5).show('text'))

corpus1 = converter.parse("wtc_part1")
measureStack = corpus1.measures(0,3)
print(measureStack.show('text'))
