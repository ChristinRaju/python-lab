registered_emails = set()

def register_user():
    while True:
        email = input("Enter your email address: ").strip().lower()

        if email in registered_emails:
            print(f"Error: {email} is already been registered.")
        else:
            registered_emails.add(email)
            print(f"Success: {email} has been successfully registered.")

        choice = input("Do you want to register another email? (yes/no): ").strip().lower()

        if choice != 'yes':
            print("Registration closed.")
            break
