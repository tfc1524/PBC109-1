def histogram( seq ):
    d = dict()
    for element in seq:
        if element not in d :
            d[element] = 1
        else:
            d[element] += 1
    return d

def invert_dict ( d ) :
    inv = dict()
    for key in d :
        val = d[ key ]
        print("val" + str(val) )
        if val not in inv :
            inv [ val ] = [ key ] 
        else :
            inv [ val ].append( key )

        print("check " + str( inv[val] ) )
    return inv

hist = histogram('parrot')
print(hist)
inverted = invert_dict( hist )
print(inverted)
