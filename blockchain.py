'''The start of the project to learn python and create a blockchain, sort of
as a goal. Hopefully I should be able to create a functioning model at the
end of this. 19 July 2020 '''
#Initializing our blockchain list
blockchain = []
open_transactions = []
owner = 'Akshay'


def get_last_value():
    #returns the last value of the blockchain
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

def add_value(sender, recipient, amount = 1.0):
    '''Appends the new transaction amount to the blockchain as well as add
    the previous transactions

    Sender: Sender of coins
    Receiver: Receiver of coins
    Amount: Total coins sent
    '''
    transaction = {
                    'sender' : sender,
                    'recipient': recipient
                    'amound' : amount
    }
    open_transactions.append(transaction)


def mine_block():
    pass

def get_transaction_value():
    '''User inputs the amount of cryptocurrency to transfer'''
    tx_recipient = input('Enter the recipient of the transaction:)
    user_input = float(input('Amount of Lightnings to trasnfer: '))
    return tx_recipient, tx_amount

def verify_chain(): #Used to verify that the chain has not been tampered with
    is_valid = True
    for block_index in range(len(blockchain)):
        #checking to see if it is the first element
        if block_index == 0:
            continue

'''Blockchain[block_index] gives us the list of the current index
, and we check the first element which should be the list
of the last chain, ie blockchain[block_index-1].
eg.
to check [[[1],2],3] with [[1],2]
so we check the first element of the currnt indext and compare
with the previous one
     '''

        elif blockchain[block_index][0] == blockchain[block_index-1]:
            is_valid = True
        else:
            is_valid = False
            break

    return is_valid

def display_blockchain():
    for block in blockchain:
        print('Current block')
        print(block)
    else:
        print('-' * 20)

def get_user_choice():
    user_input = input("Your choice:")
    return user_input



wait_input = True

while wait_input:
    print('Please choose')
    print("1: Add a new transaction")
    print("2.Display current block")
    print("3.Exit loop")
    print("4.Manipulate")
    user_choice = get_user_choice()

    if user_choice == '1':      //To be fixed
        tx_data = get_transaction_value()
        add_value(tx_data, get_last_value())

    elif user_choice == '2':
        display_blockchain()

    elif user_choice == '3':
        wait_input = False

    elif user_choice == '4':
        if len(blockchain) >= 1:
            blockchain[0] = [2]

    else:
        print('Input was valid, please pick a value from the list')
    if not verify_chain():
        print("Invalid blockchain")
        display_blockchain()
        break

else:
    print('User has stopped')
