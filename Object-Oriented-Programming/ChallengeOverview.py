'''
Create a bank account with two attributes. 
- owner
- balance

methods:
-add_owner
-add_to_balance
-remove_from_balance
    withdrawals may not exceet available balance.\
    return to initial sequence.
    instantiate your class, make several deposists and withdrawals, 
    and test to makse sure the account can't be overdrawn.

'''

class Account:
    def __init__(self, owner, username, balance):
        #account owner
        self.owner = owner
        # owners account balance
        self.balance = balance
        # username
        self.username = username
    
    #adding name to account
    def add_owner(self,name):       
        print(f'Account Name Entered: {name}')
        self.owner = self.owner + name
        print(f'Updated Account Name: {self.owner}')
    #adding a password
    def add_username(self,username):
        self.username = self.username + username
        print(f'Username created.')
    #adding a deposit
    def add_to_balance(self,deposit):
        print(f'Amount added to account: {deposit}')
        self.balance = self.balance + deposit
        print(f'Updated account balance: {self.balance}')
    #withdrawing from account.
    def remove_from_balance(self,withdrawal):
        # gotta check the balance of the account. compare it to the incoming withdrawal. 
        # if withdrawal is too much then no-go.
        if withdrawal >= self.balance:
            print(f'{withdrawal} amount exceeds current balance of: {self.balance}')
            # return withdrawal
        else: 
            print(f'Amount withdrawn from account: {withdrawal}')
            self.balance = self.balance - withdrawal
            print(f'Updated account balanace: {self.balance}')

    def __str__(self):
        return f'Account owner: {self.owner} - Account username: {self.username} - Account Balance: {self.balance}'

# accountVault = {}
#passing the account class args.  # 
account = Account('', '', 0)
#adding a name to the account
name = input('Enter your name: ')
account.add_owner(name)
print(account)
#adding a password
username= input('Enter your username: ')
account.add_username(username)
# accountVault.update(account.owner, account.username)
print(account)
# print(accountVault[0])

# deposits to the account
deposit = int(input('Enter how much to deposit: '))
account.add_to_balance(deposit)
#withdrawls to the account
withdrawal = int(input('Enter how much to withdraw: '))
account.remove_from_balance(withdrawal)
# current balance of the account
print('Current balance:', account.balance)
print(account)
# print(type(accountVault))
