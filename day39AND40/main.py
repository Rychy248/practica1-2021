"""
* APIs Required
*   Google Sheet Data Management - https://sheety.co/
*   Kiwi Partners Flight Search API (Free Signup, Requires Credit Card Details) - https://partners.kiwi.com/
*   Tequila Flight Search API Documentation - https://tequila.kiwi.com/portal/docs/tequila_api
*   Twilio SMS API - https://www.twilio.com/docs/sms
"""
from controller import Controller

def main():
    controller = Controller()
    keep_program = True

    while keep_program:
        print("Welcome to the flight Club")

        flag = True
        while flag:
            option = input("\n\nType one option:\n0-exit\n1-Register a new user\n2-Send emails, with cheapers flights\n\noptions: ")
            try:
                option = int(option)
                if 0 <= option <= 2:
                    flag = False
                else:
                    print("Invalid option, try again...")
            except:
                print("Invalid input, try again...")

        if option == 0:
            print("Bye Bye!, We hope to see you soon!")
            keep_program = False
        elif option == 1:
            response = controller.save_customer()
            print("Response: \n",response)
        elif option == 2:
            fligths = controller.send_mails_to_customers()
    

main()