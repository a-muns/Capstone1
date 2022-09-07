# This is the main file of Team 3's first capstone
import sys


def print_intro_prompt():
    # header content to be updated later on
    print(
        "CREATE A NEW REQUEST - 1\nVIEW BLOCKED REQUESTS - 2\n======================================"
    )
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

    # Placeholder variables to hold inputs (Alex K)
    referrer_ip = input("Insert refferer ip and press ENTER: ")
    host_ip = input("Insert host ip and press ENTER: ")
    user_ip = input("Insert user ip and press ENTER: ")
    user_location = input("Insert user location and press ENTER: ")
    operating_system = input("Insert operating system and press ENTER: ")
    device = input("Insert device and press ENTER: ")

    # Analyze each field as valid or invalid (Maria)
    # Valid data
    valid_referrer_url = "www.allsafe.io/security/tunnel/POD:2208"
    string_min_host_ip = '10.0.24.123'
    string_max_host_ip = '12.1.23.164'
    string_min_user_ip = '234.305.0.21'
    string_max_user_ip = '430.640.1.63'
    valid_location = "Toronto"
    valid_os = "Windows"
    valid_device = "Desktop"

    # Counter for valid fields
    counter_valid_fields = 0

    # validates referrer URL
    if referrer_ip.lower().__eq__(valid_referrer_url.lower()):
        counter_valid_fields += 1

    # validates host ip using method validate_ip
    if validate_ip(string_min_host_ip, string_max_host_ip, host_ip):
        counter_valid_fields += 1

    # validates user ip using method validate_ip
    if validate_ip(string_min_user_ip, string_max_user_ip, user_ip):
        counter_valid_fields += 1

    # validates location is Toronto
    if user_location.lower().__eq__(valid_location.lower()):
        counter_valid_fields += 1

    # validates operating system is Windows
    if operating_system.lower().__eq__(valid_os.lower()):
        counter_valid_fields += 1

    # validates device is Desktop
    if device.lower().__eq__(valid_device.lower()):
        counter_valid_fields += 1

    # True if request is valid
    is_valid = counter_valid_fields >= 3

    # Accept request or add it to blocked list based on count of valid fields (Alex M)
    if (counter_valid_fields >= 3):
        print("Request approved.")
    else:
        try:
            blocked_list = open("blocked.txt", "x")
        except FileExistsError:
            pass
        finally:
            blocked_list = open("blocked.txt", "a")
            blocked_list.write(referrer_ip)
            blocked_list.write("\n")
            blocked_list.write(host_ip)
            blocked_list.write("\n")
            blocked_list.write(user_ip)
            blocked_list.write("\n")
            blocked_list.write(user_location)
            blocked_list.write("\n")
            blocked_list.write(operating_system)
            blocked_list.write("\n")
            blocked_list.write(device)
            blocked_list.write("\n\n")
            print("Request denied. Added to blocked list.")


def view_blocked_requests():

    # Read and print blocked.txt
    try:
        read_blocked = open("blocked.txt", "r")
        print("\nBlocked requests\n================\n" + read_blocked.read())
        read_blocked.close()
    except FileNotFoundError:
        print("\nThe blocked list cannot be found.")


''' 
Validates ip address by checking that the first and last 8 bits entered by the user
are between the first and last 8 bits of the valid ip address
'''


def validate_ip(string_min_ip, string_max_ip, ip):

    # splits the min ip address string
    list_min_ip = string_min_ip.split(".")
    int_min_value1 = list_min_ip[0]  # stores the first 8 bits
    int_min_value2 = list_min_ip[3]  # stores the last 8 bits

    # splits the max ip address string
    list_max_ip = string_max_ip.split(".")
    int_max_value1 = list_max_ip[0]  # stores the first 8 bits
    int_max_value2 = list_max_ip[3]  # stores the last 8 bits

    # splits the user input ip address string
    list_user_ip = ip.split(".")
    int_first_val = list_user_ip[0]  # stores first 8 bits
    int_last_val = list_user_ip[3]  # stores last 8 bits

    # Compares first and last 8 bits of the entered ip address with the first and last 8 bits of the valid ip address
    if (int_min_value1 <= int_first_val <= int_max_value1) and \
            (int_min_value2 <= int_last_val <= int_max_value2):
        return True
    else:
        return False


print_intro_prompt()
