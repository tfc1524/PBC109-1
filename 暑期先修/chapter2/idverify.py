
def verify_twid( idstr ):
    #check length
    if len( idstr ) !=10 :
        return False

    #check第一碼
    code1 = ord( idstr[ 0 ] )
    if ( code1 < 65 or code1 > 90 ) :
        return False

    #check the remaining number
    for i in range( 1 , 10 ) :
        code2 = ord ( idstr[ i ] )
        if ( code2 < 48 or code2 > 57 ) :
            return False

    code2 = ord( idstr[ 1 ] )
    if ( code2 < 49 or code2 > 50 ):
        return False

    cmap = [ 10 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 34 , 18 , 19 , 20 , 21 , 22 , 35 , 23 , 24 , 25 , 26 , 27 , 28 , 29 , 32 , 30 , 31 , 33 ]

    num1 = cmap [ code1 - 65 ]
    newid = str(num1) + idstr[1:]

    weight = [ 1 , 9 , 8 , 7 , 6 , 5 , 4 , 3 , 2 , 1 , 1 ]
    checksum = 0

    for i in range( 0 , 11 ) :
        checksum += weight[ i ] * int( newid [ i ] )

    if checksum % 10 == 0 :
        return "ok"
    else :
        return False


id = input("enter your id :")
print( verify_twid( id ) )
