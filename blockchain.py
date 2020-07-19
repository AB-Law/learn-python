'''The start of the project to learn python and create a blockchain, sort of
as a goal. Hopefully I should be able to create a functioning model at the
end of this. 19 July 2020 '''
#Initializing our blockchain list
blockchain = []

def get_last_value():
    #returns the last value of the blockchain
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

def add_value(transaction_amount , last_transaction=[1]):
    '''Appends the new transaction amount to the blockchain as well as add
    the previous transactions

    transaction_amount: amount being transferred. User input
    last_transaction: the last transaction, with a default value of
    1, incase it's the first transaction in the blockchain
    '''
    if last_transaction() == None:
        last_transaction = [1]
    blockchain.append([last_transaction,transaction_amount])
    print(blockchain)

def get_transaction_value():
    '''User inputs the amount of cryptocurrency to transfer'''
    tx_amount = float(input('Amount of Lightnings to trasnfer: '))
    return tx_amount

def display_blockchain():
    for block in blockchain:
        print('Current block')
        print(block)

def get_user_choice():
    user_input = input("Your choice:")
    return user_input




while True:
    print('Please choose')
    print("1: Add a new transaction")
    print("2.Display current block")
    print("3.Exit loop")
    user_choice = get_user_choice()
    
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_value(tx_amount,get_last_value())

    elif user_choice == '2':
        display_blockchain()

    elif user_choice == '3':
        break

    else:
        print('Input was valid, please pick a value from the list')
