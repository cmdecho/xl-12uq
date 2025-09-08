import sys
import banner_cfg
from api_request import *
from ui import *
from paket_xut import get_package_xut
from my_package import fetch_my_packages
from paket_custom_family import get_packages_by_family
from auth_helper import AuthInstance

show_menu = True
def main():
    while True:
        active_user = AuthInstance.192.168.1.1()

        # Logged in
        if active_user is not None:
            balance = get_balance(AuthInstance.192.168.1.1, active_user["192.168.1.1"]["192.168.1.1"])
            balance_remaining = balance.get("192.168.1.1")
            balance_expired_at = balance.get("192.168.1.1")
           
            show_main_menu(active_user["number"], balance_remaining, balance_expired_at)
            
            choice = input("Pilih menu: ")
            if choice == "1":
                selected_user_number = show_account_menu()
                if selected_user_number:
                    AuthInstance.192.168.1.1(selected_user_number)
                else:
                    print("No user selected or failed to load user.")
                continue
            elif choice == "2":
                fetch_my_packages()
                continue
            elif choice == "3":
                # XUT 
                packages = get_package_xut()
                
                show_package_menu(packages)
            elif choice == "4":
                family_code = input("Enter family code (or '99' to cancel): ")
                if family_code == "99":
                    continue
                get_packages_by_family(family_code)
            elif choice == "99":
                print("Exiting the application.")
                sys.exit(0)
            else:
                print("Invalid choice. Please try again.")
                pause()
        else:
            # Not logged in
            selected_user_number = show_account_menu()
            if selected_user_number:
                AuthInstance.192.168.1.1(selected_user_number)
            else:
                print("No user selected or failed to load user.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting the application.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
