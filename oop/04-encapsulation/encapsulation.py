#encapsulation - hiding internal data and controlling access to it
#encapsulation allows us to control the access and visibility of the data and methods of a class providing a way to protect and organize the code
###############################################################
#public attributes - anyone can access and modify and anywhere to be accessed
#protected attributes - can be accessed within the class and its child classes but not outside the class
#private attributes - can only be accessed within the class and not outside the class
#solution 1 - private attributes with _ and __
class BankAccount_Better:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance      #"protected" - hint: don't touch directly
        self.__pin = 1234           #"private" - harder to access
    
    def get_balance(self):          #controlled access
        return self._balance
    
    def withdraw(self, amount, pin):
        if pin != self.__pin:
            return "Wrong PIN"
        if amount > self._balance:
            return "Insufficient funds"
        self._balance -= amount
        return f"Withdrew ${amount}. Balance: ${self._balance}"
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return f"Deposited ${amount}. Balance: ${self._balance}"
        return "Invalid amount"

account = BankAccount_Better("John", 1000)
print(account.get_balance())         #1000 - controlled access
print(account.withdraw(100, 1234))   #Withdrew $100. Balance: $900
print(account.withdraw(100, 9999))   #Wrong PIN

#still possible but harder to do by accident:
print(account._balance)              #can still access with _
# print(account.__pin)               #ERROR - name mangling makes this hard

###############################################################

#solution 2 - property decorators (pythonic way)
class BankAccount_Best:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance
        self._transaction_count = 0
    
    @property
    def balance(self):  #getter - controls how balance is accessed
        return f"${self._balance:.2f}"
    
    @balance.setter  
    def balance(self, value):  #setter - controls how balance is changed
        if isinstance(value, (int, float)) and value >= 0:
            self._balance = value
            self._transaction_count += 1
        else:
            raise ValueError("Balance must be a positive number")
    
    @property
    def transaction_count(self):  #read-only property
        return self._transaction_count
    
    def transfer_to(self, other_account, amount):
        if amount > self._balance:
            return "Insufficient funds"
        self._balance -= amount
        other_account._balance += amount  #accessing other's protected attribute
        self._transaction_count += 1
        return f"Transferred ${amount}"

account1 = BankAccount_Best("John", 1000)
account2 = BankAccount_Best("Sarah", 500)

print(account1.balance)              #$1000.00 (uses getter)
account1.balance = 1500              #uses setter
print(account1.balance)              #$1500.00

# account1.balance = -100            #ERROR - setter prevents this
# account1.balance = "invalid"       #ERROR - setter prevents this

print(f"Transactions: {account1.transaction_count}")  #read-only

###############################################################

#real-world example - user authentication system
class UserAccount:
    def __init__(self, username, password):
        self.username = username
        self._password_hash = self._hash_password(password)  #never store plain password
        self._login_attempts = 0
        self._is_locked = False
    
    def _hash_password(self, password):  #private helper method
        #in real app, use proper hashing like bcrypt
        return f"hashed_{password}"
    
    @property
    def is_locked(self):  #read-only property
        return self._is_locked
    
    def login(self, password):
        if self._is_locked:
            return "Account locked due to too many failed attempts"
        
        if self._hash_password(password) == self._password_hash:
            self._login_attempts = 0  #reset on successful login
            return "Login successful"
        else:
            self._login_attempts += 1
            if self._login_attempts >= 3:
                self._is_locked = True
                return "Too many failed attempts. Account locked."
            return f"Wrong password. {3 - self._login_attempts} attempts remaining."
    
    def change_password(self, old_password, new_password):
        if self._hash_password(old_password) != self._password_hash:
            return "Current password incorrect"
        
        if len(new_password) < 8:
            return "New password must be at least 8 characters"
        
        self._password_hash = self._hash_password(new_password)
        return "Password changed successfully"
    
    def unlock_account(self, admin_key):  #admin can unlock
        if admin_key == "admin_master_key":
            self._is_locked = False
            self._login_attempts = 0
            return "Account unlocked"
        return "Invalid admin key"

#usage - controlled access to sensitive data
user = UserAccount("john_doe", "mypassword123")

print(user.login("wrongpass"))      #Wrong password. 2 attempts remaining.
print(user.login("wrongpass"))      #Wrong password. 1 attempts remaining.  
print(user.login("wrongpass"))      #Too many failed attempts. Account locked.
print(user.login("mypassword123"))  #Account locked due to too many failed attempts

print(f"Is locked: {user.is_locked}")  #True (read-only)

#admin unlocks account
print(user.unlock_account("admin_master_key"))  #Account unlocked
print(user.login("mypassword123"))               #Login successful

###############################################################

#real-world example - configuration management
class AppConfig:
    def __init__(self):
        self._settings = {
            'debug': False,
            'max_connections': 100, 
            'timeout': 30
        }
        self._readonly_settings = {'version': '1.0.0', 'app_name': 'MyApp'}
    
    @property
    def debug(self):
        return self._settings['debug']
    
    @debug.setter
    def debug(self, value):
        if isinstance(value, bool):
            self._settings['debug'] = value
        else:
            raise ValueError("Debug must be True or False")
    
    @property  
    def version(self):  #read-only
        return self._readonly_settings['version']
    
    def get_setting(self, key):
        return self._settings.get(key, "Setting not found")
    
    def update_setting(self, key, value):
        if key in self._readonly_settings:
            return f"Cannot modify readonly setting: {key}"
        
        #validation rules
        if key == 'max_connections' and (not isinstance(value, int) or value < 1):
            return "max_connections must be positive integer"
        
        if key == 'timeout' and (not isinstance(value, int) or value < 5):
            return "timeout must be at least 5 seconds"
        
        self._settings[key] = value
        return f"Updated {key} to {value}"

config = AppConfig()
print(f"Debug mode: {config.debug}")        #False
config.debug = True                         #controlled change
print(f"Debug mode: {config.debug}")        #True

print(f"Version: {config.version}")         #1.0.0 (read-only)
# config.version = "2.0.0"                 #ERROR - no setter defined

print(config.update_setting('timeout', 60))     #Updated timeout to 60
print(config.update_setting('timeout', 2))      #timeout must be at least 5 seconds
print(config.update_setting('version', '2.0'))  #Cannot modify readonly setting: version

###############################################################

#benefits of encapsulation:
# 1. DATA PROTECTION - prevents accidental corruption
# 2. CONTROLLED ACCESS - validation before changes
# 3. HIDING COMPLEXITY - users don't need to know internals  
# 4. EASIER MAINTENANCE - change internals without breaking users
# 5. SECURITY - sensitive data stays protected

#naming conventions:
# public_var      - anyone can access/modify
# _protected_var  - "don't touch unless you know what you're doing"
# __private_var   - "really private, name gets mangled"