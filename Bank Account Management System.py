# Part 1: Object Oriented Bank System (Classes and Methods)
# 1. Define Account Classes:

class Account:
    def __init__(self,account_number : str ,balance : float ):
        self.account_number = account_number
        self.balance = balance
    def deposit(self,amount :float):
        self.balance += amount
    def withdraw(self,amount :float):
        if self.balance >= amount:
            self.balance -= amount
            return f"you still have in your wallet: {self.balance}"
        else:
            return f"you don't have enough to do this operation, you have {self.balance}"
    def get_balance(self):
        return self.balance
    def get_info_string(self):
        return self.account_number


# A current account that allows withdrawals up to the additional withdrawal limit.
class CheckingAccount(Account):
    def __init__(self, account_number : str, balance : float ,overdraft_limit : float):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit
    def withdraw(self, amount: float):
        if self.balance - amount >= -self.overdraft_limit:
            self.balance -= amount
        else:
            return "Overdraft limit exceeded"

class SavingsAccount(Account):
    def __init__(self, account_number : str, balance :float, interest_rate :float):
        super().__init__(account_number, balance)
        # interest_rate is always betweet 0 and 1. ex: 0.05 is 5%
        if interest_rate < 0 or interest_rate > 1:
            raise ValueError("interest_rate must be between 0 and 1 (ex: 0.05 is 5%)")
        self.interest_rate = interest_rate
    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"your new balance after the interest is: {self.balance}"

# 2. Define Bank Class:
class Bank:
    def __init__(self):
        self.accounts = {}
    
    def add_account(self, account: Account):
        self.accounts[account.account_number] = account
    
    def get_account(self, account_number: str):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            return "Account not found"
    
    # Object storage = the ability to use all of its functions and properties.
    # تخزين كائن = القدرة على استخدام كل دواله وخصائصه.
    def depos_it(self,account_number: str, amount:float):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            account.deposit(amount)
            return f"you deposit in your account :{amount}"
        else:
            return "Account not found"
    
    def withdraw(self,account_number: str, amount:float):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            result = account.withdraw(amount)
            if result is None:
                return f"Withdrawal successful. New balance: {account.get_balance()}"
            else:
                return result
        else:
            return "Account not found"
    
    def get_account_balance(self,account_number: str):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            return account.get_balance()
        else:
            return f"Account not found"
    
    def remove_account(self, account_number: str):
        if account_number in self.accounts:
            del self.accounts[account_number]
        else:
            return "Account not found"
    
    def list_accounts(self):
        for acc_number, account in self.accounts.items():
            print(f"Account Number: {acc_number}, Balance: {account.balance}")

# 3. Results to show:
my_bank = Bank()
# CheckingAccount
check1 = CheckingAccount("C001" ,1000 ,200 )
check2 = CheckingAccount("C002" ,1500 ,300 )
check3 = CheckingAccount("C003" ,2000 ,400 )
check4 = CheckingAccount("C004" ,1700 ,350 )
# SavingsAccount
save1 = SavingsAccount("S001" ,1000 ,0.02 )
save2 = SavingsAccount("S002" ,1500 ,0.04 )
save3 = SavingsAccount("S003" ,2000 ,0.06 )
# Add accounts to my_bank
my_bank.add_account(check1)
my_bank.add_account(check2)
my_bank.add_account(check3)
my_bank.add_account(check4)
my_bank.add_account(save1)
my_bank.add_account(save2)
my_bank.add_account(save3)

# a/ Deposits
print(my_bank.depos_it("C001", 500))
print(my_bank.depos_it("S003", 1000))

# b/ Withdrawals
print(my_bank.withdraw("C002", 300))
print(my_bank.withdraw("C003", 3000))
print(my_bank.withdraw("S001",2000))


# c/ Interest Addition
print(save1.add_interest())
print(save2.add_interest())
print(save3.add_interest())

# Part 2: Data Processing with map(),filter(),reduce()
# 1. map()
# this use the [get_account_balance] in the accounts.keys (with class Bank)
balances = list(map(my_bank.get_account_balance, my_bank.accounts.keys()))
print(balances)

# this use the [get_balance] in the accounts.values (with class Account)
balances1 = list(map(lambda acc: acc.get_balance(), my_bank.accounts.values()))
print(balances1)

# 2. filter()
filtered_accounts = list(filter(lambda x: x>=1500, balances))
print(f"the accounts they have greater or equale than 1500 is: {filtered_accounts}")

# 3. reduce()
from functools import reduce
total_balance = reduce(lambda x,y: x+y , balances)
print(f"total balance of all accounts in the bank : {total_balance} $")

# Part 3: Account Organization with a Tree Data Structure
# 1. Implement Tree Structure:

class TreeNode:
    def __init__(self, value):
        self.value = value  # e.g., "CheckingAccount", "SavingsAccount"
        self.children = {}  # Dictionary to store child nodes, key: child value, value: TreeNode
        self.accounts = []  # List of Account objects associated with this node

class AccountTree:
    def __init__(self):
        self.root = TreeNode("Root")  # Root node for the tree

    def add_account(self, account_object:Account):
        category = account_object.__class__.__name__  # What is the name of the class from which this object was created?
        
        if category not in self.root.children: # if the category not in self.children {} creat it.
            self.root.children[category] = TreeNode(category) # This line creates a new node in the tree and store it in [children dict] {"category": TreeNode("CheckingAccount")}.
        
        self.root.children[category].accounts.append(account_object) # it's mean: Add this account to the list of accounts belonging to this category within the tree.

    def find_accounts(self, category_name):
        if category_name in self.root.children:
            return self.root.children[category_name].accounts # Grap and return the list of accounts with same category.
        return []
    

# 2. Results to show:

my_tree = AccountTree()
for accounts in my_bank.accounts.values():
    my_tree.add_account(accounts)

checking_accounts = my_tree.find_accounts("CheckingAccount")
savings_accounts  = my_tree.find_accounts("SavingsAccount")

print("Checking Accounts:")
for acc in checking_accounts:
    print(f"- Number: {acc.account_number}, Balance: {acc.balance}")

print("Savings Accounts:")
for acc in savings_accounts:
    print(f"- Number: {acc.account_number}, Balance: {acc.balance}")

# Part 4: Data Persistence (File I/O)
# 1. Transform representation (Optional)
# creat a method and add it in class Account
def to_dict(self):
    return {
        "type": self.__class__.__name__,
        "account_number": self.account_number,
        "balance": self.balance
    }

Account.to_dict = to_dict

# Print all account type and account number, balance with to_dict() method.
for account in my_bank.accounts.values():
    print(account.to_dict())

# 2. Save Functionality in Bank:
def save_data(self, filename='bank_data.txt'):
    with open(filename, 'w') as f:
        for account in self.accounts.values():  # do a to_dict() method to all accounts.
            account_data = account.to_dict() # Turn every object into a dictionary.
            line = f"{account_data}\n"
            f.write(line) # Write each account as a single line of text in the file.
    return f"All accounts saved to {filename}"

# 3. Results to show:
Bank.save_data = save_data
my_bank.save_data("My_Bank save file.txt")
