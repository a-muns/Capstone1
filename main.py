# This is the main file of Team 3's first capstone
import sys


def print_intro_prompt():
    # header content to be updated later on
    print("CREATE A NEW REQUEST - 1\nVIEW BLOCKED REQUESTS - 2\n======================================")
    user_input = input("Select an option: ")
    if user_input == "1":
        create_request()
    elif user_input == "2":
        view_blocked_requests()
    elif user_input == "q":
        sys.exit()
    else:
        print("\nInvalid option!")
        print_intro_prompt()


def create_request():
    print("<create request logic>")
  
    # Placeholder variables to hold inputs:
    referrer_ip = 0
    host_ip = 0
    user_ip = 0
    user_location = 0
    operating_system = 0
    device = 0

    # Save values to unique .txt file

    # Read .txt file

    # Analyze each field as valid or invalid
  
    # Accept request or add it to blocked list based on count of valid fields 
    

def view_blocked_requests():

    # Read and print blocked.txt
    try:
      read_blocked = open("blocked.txt", "r")
      print("\n", read_blocked.read())
      read_blocked.close()
    except FileNotFoundError: 
      print("\nThe blocked list cannot be found.")


print_intro_prompt()
