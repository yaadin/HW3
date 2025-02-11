Personal Account Management
Purpose
This project defines a simple bank account system with deposit and withdrawal functionalities. It includes classes for handling transactions and keeping track of the account's balance and transaction history.

Classes and Methods
1. Amount Class
The Amount class represents a transaction and stores details about the amount, transaction type, and the timestamp of the transaction.
+Method __str__(self): Returns a string representation of the transaction in the format

2. PersonalAccount Class
The PersonalAccount class represents a bank account that holds an account number, account holder's name, balance, and transaction history.
Method deposit(self, amount): Deposits a specified amount into the account and records the transaction.

Method withdrowal(self, amount): Withdraws a specified amount from the account if sufficient funds are available. Returns an error message if insufficient funds.

Method print_transaction_history(self): Prints the history of all transactions made (deposits and withdrawals).

Method get_balance(self): Returns the current balance of the account.

Method get_account_number(self): Returns the account number.

Method set_account_number(self, account_number): Sets a new account number.

Method get_account_holder(self): Returns the name of the account holder.

Method set_account_holder(self, account_holder): Sets a new account holder name.

Method __str__(self): Returns a string representation of the account details, including the account holder's name, account number, and balance.

Method __add__(self, amount): Implements the addition operator (+) to deposit the specified amount into the account.

Method __sub__(self, amount): Implements the subtraction operator (-) to withdraw the specified amount from the account.


TESTS 

Deposit Money

Description: This test case checks if the deposit method correctly increases the account balance. It involves calling the deposit method with an amount.
Withdraw Money

Description: This test case checks if the withdrawal method correctly decreases the account balance when sufficient funds are available. It involves calling the withdrowal method with an amount.
Insufficient Funds for Withdrawal

Description: This test case checks if the system handles attempts to withdraw more than the available balance. It involves calling the withdrowal method with an amount greater than the current balance.
Print Transaction History

Description: This test case checks if the print_transaction_history method correctly prints all transactions (deposits and withdrawals). It involves calling this method after performing a few transactions.
Check Account Balance and Transaction History

Description: This test case checks if the account balance and transaction history are correctly maintained after multiple transactions. It involves calling get_balance and print_transaction_history after several deposits and withdrawals.


Everything works as intended for all these scenarios.

