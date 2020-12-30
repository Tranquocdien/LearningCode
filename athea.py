def emailProcess():
    while True:
        email = input("Please enter your email address: ").strip()
        if email:
            email_username = email[0:email.index("@")]
            email_domain = email[email.index("@")+1:]
            print(f"Username is {email_username}")
            print(f"Emaildomain is {email_domain}")
            break
        else:
            print("Your emailaddress is empty. Please try again")
            continue
            



def main():
    emailProcess()




if __name__ == "__main__":
    main()

 


