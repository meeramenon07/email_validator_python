from email_validator import validate_email, EmailNotValidError   
email = "johndoe@gmail.com"
is_valid_email = validate_email(email)
if is_valid_email: 
    print("Email is valid!")
else:
    print("Email is not valid!")
    


