from athea import emailProcess, printemail


def main():
    emails = ("helloworld@Coderisme.com", "tranquocdien2002@gmail.com", "localspo@gmail.com")
    for email in emails:
        email_username, email_domain = emailProcess(email)
        printemail(email_username, email_domain)


if __name__ == "__main__":
    main()

