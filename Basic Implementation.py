'''The start of the project to learn python and create a blockchain, sort of
as a goal. Hopefully I should be able to create a functioning model at the
end of this. 19 July 2020 '''
#Initializing our blockchain list
blockchain = []

def get_last_value():
    #returns the last value of the blockchain
    return blockchain[-1]

def add_value(transaction_amount , last_transaction=[1]):
    '''Appends the new transaction amount to the blockchain as well as add
    the previous transactions

    transaction_amount: amount being transferred. User input
    last_transaction: the last transaction, with a default value of
    1, incase it's the first transaction in the blockchain
    '''
    blockchain.append([last_transaction,transaction_amount])
    print(blockchain)

def get_user_transaction():
    '''User inputs the amount of cryptocurrency to transfer'''
    tx_amount = float(input('Amount of Lightnings to trasnfer: '))
    return tx_amount



add_value(get_user_transaction())
add_value(get_user_transaction())
add_value(get_user_transaction())
