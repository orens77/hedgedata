#!/usr/local/bin/python3
from hedgeme import Data, symbols
from arctic import Arctic

a = Arctic('localhost')

d = Data(a)
d.cache(symbols())
