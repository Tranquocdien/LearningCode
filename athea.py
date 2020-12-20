def emailProcess(email):
    email_username = email[0:email.index("@")]
    email_domain = email[email.index("@")+1:]
    return email_username, email_domain
    

def printemail(email_username, email_domain):
    print(f"Username is {email_username}")
    print(f"Emaildomain is {email_domain}")



def main():
    email = input("Please enter your email address: ").strip()
    email_username, email_domain = emailProcess(email)
    printemail(email_username, email_domain)


if __name__ == "__main__":
    main()

 


