import getpass

# ---------------- USER CLASS ---------------- #
class User:
    users_db = {}

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.has_voted = False

    @classmethod
    def add_user(cls, username, password):
        if username in cls.users_db:
            print("Username already exists. Please try a different username.")
            return False
        cls.users_db[username] = User(username, password)
        return True

    @classmethod
    def authenticate(cls, username, password):
        user = cls.users_db.get(username)
        if user and user.password == password:
            return user
        return None


def register_user():
    username = input("Enter a username: ")
    password = getpass.getpass("Enter password: ")
    if User.add_user(username, password):
        print("User registered successfully!")
    else:
        print("Registration failed!")


def login_user():
    username = input("Enter a username: ")
    password = getpass.getpass("Enter password: ")
    user = User.authenticate(username, password)
    if user:
        print("Login successful!")
        return user
    else:
        print("Invalid username or password.")
        return None


# ---------------- VOTING SYSTEM ---------------- #
class VotingSystem:
    def __init__(self):
        self.parties = {"A": 0, "B": 0, "C": 0}

    def vote(self):
        username = input("Enter your username to vote: ")
        password = getpass.getpass("Enter your password to vote: ")
        user = User.authenticate(username, password)
        if user:
            if user.has_voted:
                print("You have already voted!")
                return
            print("Parties: A , B , C")
            choice = input("Enter the party name you want to vote for: ").upper()
            if choice in self.parties:
                self.parties[choice] += 1
                user.has_voted = True
                print("Vote successfully recorded!")
            else:
                print("Invalid party choice!")
        else:
            print("Invalid username or password!")

    def view_results(self):
        print("\nVoting Results:")
        for party, votes in self.parties.items():
            print(f"Party {party}: {votes} Votes")


# ---------------- MAIN PROGRAM ---------------- #
def main():
    voting_system = VotingSystem()
    while True:
        print("\n--- Voting System Menu ---")
        print("1. Register")
        print("2. Login")
        print("3. Vote")
        print("4. View Results")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if choice == 1:
            register_user()
        elif choice == 2:
            login_user()
        elif choice == 3:
            voting_system.vote()
        elif choice == 4:
            voting_system.view_results()
        elif choice == 5:
            print("Exiting the program...")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
