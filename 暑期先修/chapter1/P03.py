account1 = int ()
account2 = int ()
transfer = int ()

print ( "Enter the account balance of account 1 :" )
account1 = int ( input () )
print ( "Enter the account balance of account 2 :" )
account2 = int ( input () )

print ( "Enter the amount of money which would be transferred from the former to the latter :" )
transfer = int ( input () )

if transfer > account1 :
    account2 += account1
    account1 = 0
else :
    account1 -= transfer
    account2 += transfer

print ( "The balance of the two accounts are : "  , account1 , account2 )
