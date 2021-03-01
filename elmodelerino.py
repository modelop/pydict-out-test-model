#fastscore.slot.0: in-use
#fastscore.slot.1: in-use

import time

#modelop.score
def action(datum):
    print(datum, flush=True)
    time.sleep(1)
    i = datum['i']
    out = {
            'integer' : 123 * i,
            'float' : 123.456 + i,
            'boolean': i % 2 == 0,
            'string': 'thequickbrownfoxjumpedoverthelazydog'[0:i]
            }
    yield out

#x = action({'i': 5})
#print(next(x))
#x = action({'i': 12})
#print(next(x))
