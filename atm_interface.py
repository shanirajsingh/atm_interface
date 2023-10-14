class User:
    def __init__(self,user_id,pin):
        self.user_id = user_id
        self.pin = pin
        self.balance = 1000  # Initial balance for each user
        self.transaction_history=[]

class ATM:
    def __init__(self):
        self.users = {}  # Dictionary to store user data
        
    def add_user(self, user_id, pin):
        if user_id not in self.users:
            user=User(user_id,pin)
            self.users[user_id]=user    
            print(f"User {user_id} has been created successfully.")
            self.login(user_id,pin)    
        else:
            print("User already exists.")

    def login(self, user_id, pin):
        if user_id in self.users and self.users[user_id].pin == pin:
            return self.users[user_id]
        else:
            return None

    def withdraw(self, user, amount):
        if user.balance >= amount:
            user.balance -= amount
            user.transaction_history.append(f"Withdraw ${amount}")
            print(f"Withdrew ${amount}. New balance: ${user.balance}")
        else:
            print("Insufficient balance.")

    def deposit(self, user, amount):
        user.balance += amount
        user.transaction_history.append(f"Deposit ${amount}")
        print(f"Deposited ${amount}. New balance: ${user.balance}")

    def transfer(self, user, recipient_id, amount):
        if recipient_id in self.users:
            recipient = self.users[recipient_id]
            if user.balance >= amount:
                user.balance -= amount
                recipient.balance += amount
                user.transaction_history.append(f"Transfer {amount} to {recipient_id}")
                print(f"Transferred ${amount} to User {recipient_id}. New balance: ${user.balance}")
            else:
                print("Insufficient balance for transfer.")
        else:
            print("Recipient not found.")
    
    def show_balance(self,user):
        return f"Current Balance: ${user.balance}"
    
    def show_transaction_history(self,user):
        if len(user.transaction_history)==0:
            return("No transaction history!")            
        else:
            return "\n".join(user.transaction_history)
def main():
    atm = ATM()
    atm.add_user("user123", "1234")  # Dummy user
    atm.add_user("user456", "5678")  # Dummy user

    while True:
        print("\nATM Menu:")
        print("1. Login")
        print("2. Sign In")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            user_id = input("Enter user ID: ")
            pin = input("Enter PIN: ")
            user = atm.login(user_id, pin)
        elif choice == "2":
            print("***Enter your Sign In Details***")
            user_id=input("Enter User_id:")
            pin=input("Enter Pin:")
            atm.add_user(user_id,pin)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")
            break
            
        if user:
            while True:
                print("\nUser Menu:")
                print("1. Transactions History")
                print("2. Withdraw")
                print("3. Deposit")
                print("4. Transfer")
                print("5. Check_Balance")
                print("6. Quit")
                user_choice = input("Enter your choice: ")

                if user_choice == "1":
                    print(atm.show_transaction_history(user))
                elif user_choice == "2":
                    amount = float(input("Enter amount to withdraw: "))
                    atm.withdraw(user, amount)
                elif user_choice == "3":
                    amount = float(input("Enter amount to deposit: "))
                    atm.deposit(user, amount)
                elif user_choice == "4":
                    recipient_id = input("Enter recipient's user ID: ")
                    amount = float(input("Enter amount to transfer: "))
                    atm.transfer(user, recipient_id, amount)
                elif user_choice == "5":
                    print(atm.show_balance(user))
                elif user_choice == "6":
                    print("THANK YOU FOR USING ATM")
                    break
                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Login failed. Please try again.")

if __name__ == "__main__":
    main()
