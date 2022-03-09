class User:
    def __init__(self, first_name, last_name, gender, street_address, city,
                 email, cc_number, cc_type, balance, account_no):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.street_address = street_address
        self.city = city
        self.email = email
        self.cc_number = cc_number
        self.cc_type = cc_type
        self.balance = balance
        self.account_no = account_no
        user_list.append(self)

    def display_info(self):
        print("First name:", self.first_name)
        print("Last name:", self.last_name)
        print("Gender:", self.gender)
        print("Address:", self.street_address)
        print("City:", self.city)
        print("Email:", self.email)
        print("cc_number", self.cc_number)
        print("cc_type", self.cc_type)
        print("Balance:", self.balance)
        print("Account number:", self.account_no)
        print("______________________________________")


def generate_users():
    import csv
    with open('bankUsers.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',', quotechar="'")
        for line in filereader:
            User(line[0], line[1], line[2], line[3], line[4], line[5], line[6],
                 line[7], float(line[8][1:]), line[9])


# Find a user
def find_user():
    user_to_find = input("Enter the name of the user: ").title()
    for user in user_list:
        if user.first_name == user_to_find:
            print(f"Hi {user_to_find}")
            print(f"This is the information of {user_to_find}. "
                  f"{user.display_info()}")
            return user
    else:
        print("Sorry, no user was found with that name.")


def overdrafts():
    overdraft_list = []
    overdraft_amount = 0
    for user in user_list:
        if user.balance <= 0:
            overdraft_amount += user.balance
            overdraft_list.append(user)

    print(f"There is a total of {len(overdraft_list)} users with an overdraft, totalling "
          f"${overdraft_amount.__round__(2)}.")
    print("---------------------------------------------")
    print("This is a list of all users with an overdraft")
    print("---------------------------------------------")
    for overdraft_user in overdraft_list:
        overdraft_user.display_info()



def missingEmails():
    count_missing_emails = True
    for user in user_list:
        if not user.email:
            user.display_info()
            count_missing_emails += 1 # it takes out the missing email users and calculate total with emails
    print(f"The total number of users without emails are {count_missing_emails}")



def bankDetails(): # solutions
    count_user = 0 # 0 mean removing original counting user to set into new (always do that)
    total_worth = 0
    highest_balance = ["", 0]
    lowest_balance = ["", 0]
    for user in user_list:
        name = user.first_name + "" + user.last_name
        count_user += 1
        total_worth += user.balance
        if user.balance < lowest_balance[1]:
            lowest_balance = [name, user.balance]
        elif user.balance  == lowest_balance[1]:
            lowest_balance.append([name, user.balance])
        elif lowest_balance > highest_balance[1]:
            highest_balance = [name, user.balance]
        elif user.balance == highest_balance[1]:
            highest_balance.append([name, user.balance])
    print(f"\nThe total number of users is : {count_user}"
          f"\nThe total worth of the banks is ${round(total_worth,2)}"
          f"\nThe customers with the highest balance is:\n"
          f"\t\t{highest_balance[0]} ${highest_balance[1]}"
          f"\nThe customers with the lowest balance is:\n"
          f"\t\t{lowest_balance[0]} ${lowest_balance[1]}")
    # try understand the print function more




# Number checking function
# Get's the scale factor - which must be a number
def num_check(text):
    error = "Must be an integer!"
    valid = False
    while not valid:
        try:
            response = int(input(text))
            if isinstance(num_check, int):
                print(error)
                valid = True
                return num_check
        except ValueError:
            print(error)


def transfer():
# TO COMPLETE

    True



user_list = []
generate_users()

userChoice = ""
print("Welcome!")

while userChoice != "Q":
    print("What function would you like to run?")
    print("Type 1 to find a user")
    print("Type 2 to print overdraft information")
    print("Type 3 to print users with missing emails")
    print("Type 4 to print bank details")
    print("Type 5 to transfer money")
    print("Type Q to quit")
    userChoice = input("Enter choice: ".upper())
    print()

    if userChoice == "1":
        find_user()
    elif userChoice == "2":
        overdrafts()
    elif userChoice == "3":
        missingEmails()
    elif userChoice == "4":
        bankDetails()
    elif userChoice == "5":
        transfer()
    print()
